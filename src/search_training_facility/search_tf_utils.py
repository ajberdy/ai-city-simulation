from sgqlc.operation import Operation
from graphql_schema import graphql_schema as schema
from src.graphql_utils import endpoint

op = Operation(schema.Query)

"""
query {
  searchTf {
    id
    roadGraph {
      name
    }
  }
}
"""


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

print(get_map())
