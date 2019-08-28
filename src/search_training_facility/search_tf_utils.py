from enum import Enum, auto

from sgqlc.operation import Operation
from graphql_schema import graphql_schema as schema
from src.graphql_utils import endpoint


def get_map():
    """ get the map from the server """
    op = Operation(schema.Query)
    search_tf = op.search_tf()

    road_graph = search_tf.road_graph()
    road_graph.name()

    connections = road_graph.connections()
    connections.index()
    connections.start()
    connections.end()
    connections.direction()

    intersections = road_graph.intersections()
    intersections.index()
    intersections.x()
    intersections.y()
    intersections.connections()

    data = endpoint(op)
    result = op + data

    return result.search_tf.road_graph


class SearchState:
    __slots__ = ("last_intersection", "distance_since", "direction")


class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


def direction_to_orientation(current_orientation, turn_direction):
    """ convert turn relative direction to new absolute orientation """
    orientations = [
        schema.Direction.NORTH,
        schema.Direction.EAST,
        schema.Direction.SOUTH,
        schema.Direction.WEST
    ]
    current_orientation_index = orientations.index(current_orientation)

    if turn_direction == schema.RelativeDirection.STRAIGHT:
        return current_orientation

    if turn_direction == schema.RelativeDirection.LEFT:
        return orientations[current_orientation_index - 1]

    if turn_direction == schema.RelativeDirection.RIGHT:
        return orientations[(current_orientation_index + 1) % 4]


# print(get_map())
# print(direction_to_orientation("EAST", "LEFT"))
