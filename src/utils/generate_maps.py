MAP = \
"""
 * = = 1c = = 2a
               |
               *
"""

NORTH, SOUTH, EAST, WEST = "NORTH", "SOUTH", "EAST", "WEST"


def string_to_map(string):
    """
    convert map text file to json string

    map:
    * = car sink / source
    n = car on road, facing north
    e = car on road, facing east
    s = car on road, facing south
    w = car on road, facing west


    | north/south connection
    = east/west connection

    [int][letter] = intersection with period proportionate to letter, phase given by number

    graph:
    {
      intersections: [
        {
          index: Int
          name: String
          x: Int
          y: Int
          connections: [Int]  // connection indices
        },
        ...
      ],
      connections: [
        {
          index: Int
          start: Int  // intersection indices
          end: Int
          length: Int
          direction: Direction  // NORTH SOUTH EAST WEST
        }
      ]
    }
    """

