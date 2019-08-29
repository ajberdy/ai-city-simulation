from sgqlc.operation import Operation
from graphql_schema import graphql_schema as schema
from src.graphql_utils import endpoint

from src.search_training_facility.search_tf_utils import direction_to_orientation, \
    opposite_orientation


class CarState:

    def __init__(self, last_intersection, distance_since, direction):
        """
        initialize a new state of the car with the given parameters

        :param last_intersection: (x, y) coordinates of last intersection the car passed through
        :param distance_since: how long it has traveled since passing through last_intersection
        :param direction: which direction it has been moving since passing though last_intersection
        """
        self.last_intersection = last_intersection
        self.distance_since = distance_since
        self.direction = direction

    def __iter__(self):
        return iter((self.last_intersection, self.distance_since, self.direction))

    def __repr__(self):
        return f"CarState(last_intersection={self.last_intersection}, distance_since={self.distance_since}, " \
               f"direction={self.direction})"


class SearchTfState:
    __slots__ = (
        "_road_graph",
        "_intersections",
        "_connections",
        "_starting_car_state",
        "_update_buffer"
    )

    def __init__(self):
        self._road_graph = None
        self._intersections = None
        self._connections = None
        self._update_buffer = []

    @property
    def road_graph(self):
        if self._road_graph is not None:
            return self._road_graph
        return self.get_map()

    @property
    def intersections(self):
        if self._intersections is not None:
            return self._intersections
        return dict(
            (intersection.name, intersection) for intersection in self.road_graph.intersections
        )

    @property
    def connections(self):
        if self._connections is not None:
            return self._connections
        return dict(
            (connection.index, connection) for connection in self.road_graph.connections
        )

    @property
    def starting_car_state(self):
        start_state = self.road_graph.start_state
        return CarState(start_state.last_intersection, start_state.distance_since, start_state.direction)

    @property
    def time(self):
        return len(self._update_buffer)

    def reset(self):
        """ reset state """
        self._road_graph = None
        self._intersections = None
        self._connections = None

    def get_map(self):
        """ get the map from the server """
        op = Operation(schema.Query)
        search_tf = op.search_tf()

        road_graph = search_tf.road_graph()
        road_graph.name()

        connections = road_graph.connections()
        connections.index()
        connections.start()
        connections.end()
        connections.start_name()
        connections.end_name()
        connections.length()
        connections.direction()

        intersections = road_graph.intersections()
        intersections.index()
        intersections.name()
        intersections.x()
        intersections.y()
        intersections.connections()

        start_state = road_graph.start_state()
        start_state.last_intersection()
        start_state.distance_since()
        start_state.direction()

        data = endpoint(op)
        result = op + data

        self._road_graph = result.search_tf.road_graph
        return self._road_graph

    def get_current_road(self, state):
        """
        Get the road that the car is on, given its state

        :param state: CarState
        :return: Connection
        """
        last_intersection, distance_since, direction = state
        roads = self.get_outward_roads(last_intersection)
        return next(road for road in roads if road.direction == direction)

    def get_outward_roads(self, intersection, direction=None):
        """
        get outward roads from given intersection

        :param intersection: (x, y) coordinates of an intersection
        :param direction: Direction - if given, function will only return roads that can be turned onto
        entering the intersection from the specified direction
        :return: [Connection]
        """
        def direction_check(road):
            """ checks if a road has a turn-onto-able direction """
            if direction is None:
                return True

            return opposite_orientation(road.direction) != direction

        intersection = self.intersections[intersection]
        roads = [self.connections[ix] for ix in intersection.connections]
        return [road for road in roads if direction_check(road)]

    def append_update(self, update):
        """
        append an update to the update buffer

        :param update: CarState
        :return:
        """
        self._update_buffer.append((self.time, update))

    def push_updates(self):
        """
        push update buffer to database in order to be rendered by the graphics

        :return:
        """
        times, updates = zip(*self._update_buffer)
        intersections, distances, directions = zip(*updates)
        print(times)
        print(intersections)

        op = Operation(schema.Mutation)
        update = op.push_update_buffer(
            times=times,
            intersections=intersections,
            distances=distances,
            directions=directions
        )

        update.time()
        new_car_loc = update.new_car_loc()
        new_car_loc.intersection()
        new_car_loc.distance()
        new_car_loc.direction()

        data = endpoint(op)
        result = op + data

        print(result)
        return result

