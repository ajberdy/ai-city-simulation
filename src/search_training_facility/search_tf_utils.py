from graphql_schema import graphql_schema as schema


def direction_to_orientation(current_orientation, turn_direction):
    """ convert turn relative direction to new absolute orientation """
    orientations = [
        schema.Direction.NORTH,
        schema.Direction.EAST,
        schema.Direction.SOUTH,
        schema.Direction.WEST
    ]

    try:
        current_orientation_index = orientations.index(current_orientation)
    except ValueError:
        raise ValueError("Invalid current orientation")

    if turn_direction == schema.RelativeDirection.STRAIGHT:
        return current_orientation

    if turn_direction == schema.RelativeDirection.LEFT:
        return orientations[current_orientation_index - 1]

    if turn_direction == schema.RelativeDirection.RIGHT:
        return orientations[(current_orientation_index + 1) % 4]

    raise TypeError("Invalid turn direction")


def opposite_orientation(orientation):
    """ return opposite orientation """
    orientations = [
        schema.Direction.NORTH,
        schema.Direction.EAST,
        schema.Direction.SOUTH,
        schema.Direction.WEST
    ]

    try:
        orientation_index = orientations.index(orientation)
    except ValueError:
        raise ValueError("Invalid current orientation")

    return orientations[orientation_index - 2]


RELATIVE_DIRECTIONS = [
    schema.RelativeDirection.STRAIGHT,
    schema.RelativeDirection.LEFT,
    schema.RelativeDirection.RIGHT
]