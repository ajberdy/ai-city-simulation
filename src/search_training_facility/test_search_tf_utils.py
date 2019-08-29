import unittest
from src.search_training_facility.search_tf_utils import direction_to_orientation, opposite_orientation
from graphql_schema import graphql_schema as schema


class MyTestCase(unittest.TestCase):
    def test_direction_to_orientation(self):
        self.assertEqual("NORTH", direction_to_orientation("EAST", "LEFT"))
        self.assertEqual("EAST", direction_to_orientation("SOUTH", "LEFT"))
        self.assertEqual("SOUTH", direction_to_orientation("WEST", "LEFT"))
        self.assertEqual("WEST", direction_to_orientation("NORTH", "LEFT"))

        self.assertEqual("NORTH", direction_to_orientation("WEST", "RIGHT"))
        self.assertEqual("EAST", direction_to_orientation("NORTH", "RIGHT"))
        self.assertEqual("SOUTH", direction_to_orientation("EAST", "RIGHT"))
        self.assertEqual("WEST", direction_to_orientation("SOUTH", "RIGHT"))

        self.assertEqual("NORTH", direction_to_orientation("NORTH", "STRAIGHT"))
        self.assertEqual("EAST", direction_to_orientation("EAST", "STRAIGHT"))
        self.assertEqual("SOUTH", direction_to_orientation("SOUTH", "STRAIGHT"))
        self.assertEqual("WEST", direction_to_orientation("WEST", "STRAIGHT"))

    def test_direction_to_orientation_raises(self):
        with self.assertRaises(ValueError):
            direction_to_orientation("Not NORTH", "STRAIGHT")
            direction_to_orientation("NORTH", "not STRAIGHT")

    def test_opposite_orientation(self):
        self.assertEqual("NORTH", opposite_orientation("SOUTH"))
        self.assertEqual("SOUTH", opposite_orientation("NORTH"))
        self.assertEqual("EAST", opposite_orientation("WEST"))
        self.assertEqual("WEST", opposite_orientation("EAST"))

    def test_string_to_enum(self):
        self.assertEqual("NORTH", schema.Direction.NORTH)
        self.assertEqual("EAST", schema.Direction.EAST)
        self.assertEqual("SOUTH", schema.Direction.SOUTH)
        self.assertEqual("WEST", schema.Direction.WEST)

        self.assertEqual("STRAIGHT", schema.RelativeDirection.STRAIGHT)
        self.assertEqual("LEFT", schema.RelativeDirection.LEFT)
        self.assertEqual("RIGHT", schema.RelativeDirection.RIGHT)


if __name__ == '__main__':
    unittest.main()
