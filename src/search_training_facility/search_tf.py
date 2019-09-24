import logging

from graphql_schema import SearchAlgorithm
from src.search_training_facility.cached_local_state import SearchTfState, CarState
from src.search_training_facility.search_tf_utils import direction_to_orientation, RELATIVE_DIRECTIONS


class SearchTrainingFacility:
    """
    Class for the Search Training Facility within the AI City Simulation

    State is maintained as a SearchTfState variable, which gets the state
    from the server and keeps a local cached state.
    """

    def __init__(self):
        # facility state takes care of metadata such as the road graph and starting location
        self.facility_state = SearchTfState()
        self.car_state = CarState(*self.facility_state.starting_car_state)

    def reset_facility_state(self):
        """ clear local state cache """
        self.facility_state.reset()

    def move_car(self, action):
        """
        Get the resulting next state from performing the action in the given state

        :param state: a SearchState
        :param action: a Direction
        :return: next_state
        """
        last_intersection, distance_since, direction = self.car_state
        road = self.facility_state.get_current_road(self.car_state)

        if 0 < distance_since < road.length:
            self.car_state = CarState(last_intersection, distance_since + 1, direction)

            self.append_current_state()
            return

        if distance_since == road.length:
            new_intersection = road.end_name
            next_roads = self.facility_state.get_outward_roads(new_intersection, direction)
            next_orientation = direction_to_orientation(direction, action)
            try:
                next_road = next(road for road in next_roads if road.direction == next_orientation)
            except StopIteration:
                logging.debug(f"Not a valid action in current state: {action}, {self.car_state}")
                raise ValueError(f"Not a valid action in current state: {action}, {self.car_state}")
            new_last_intersection = next_road.start_name
            new_distance_since = 1
            new_direction = next_road.direction
            self.car_state = CarState(new_last_intersection, new_distance_since, new_direction)
            self.append_current_state()
            return

        raise IndexError("Distance since last intersection must be in [1, road_length]")    # this shouldn't happen

    def get_next_states(self, state):
        """
        Get the resulting next state from performing the action in the given state

        :param state: a SearchState
        :return: next_state
        """
        last_intersection, distance_since, direction = state
        road = self.facility_state.get_current_road(state)

        if 1 < distance_since < road.length:
            return CarState(last_intersection, distance_since + 1, direction)

        if distance_since == road.length:
            new_intersection = road.end_name
            next_roads = self.facility_state.get_outward_roads(new_intersection, direction)
            if not next_roads:
                return {}

            new_last_intersection = next_roads[0].start_name
            new_distance_since = 1

            transitions = {}

            for action in RELATIVE_DIRECTIONS:
                new_orientation = direction_to_orientation(direction, action)
                next_state = CarState(new_last_intersection, new_distance_since, new_orientation)
                transitions[action] = next_state

            return transitions

        raise IndexError("Distance since last intersection must be in [1, road_length]")

    def random_move(self, max_moves=100):
        # self.set_search_algorithm(SearchAlgorithm.BREADTH_FIRST_SEARCH)
        self.set_search_algorithm(SearchAlgorithm.RANDO_TRAVERSAL)

        moves = 0
        while True:
            if moves == max_moves:
                return
            moves += 1
            print(f"current state: {self.car_state}")
            for action in RELATIVE_DIRECTIONS:
                try:
                    self.move_car(action)
                    print(f"moved {action}")
                    break
                except ValueError:
                    print(f"can't move {action}")
            else:
                break

    def append_current_state(self):
        self.facility_state.append_update(self.car_state)

    def depth_first_search(self):
        pass

    def set_search_algorithm(self, algorithm):
        self.facility_state.set_search_algorithm(algorithm)


search_training_facility = SearchTrainingFacility()
# print(search_training_facility.facility_state.road_graph)
# print(search_training_facility.facility_state.intersections)
# print(search_training_facility.facility_state.connections)

state = CarState((0, 6), 5, "SOUTH")
# print(search_training_facility.car_state)
# print(state)
# print(search_training_facility.get_next_states(state))
# print(search_training_facility.get_next_states(state))

search_training_facility.random_move()
search_training_facility.facility_state.push_updates()
