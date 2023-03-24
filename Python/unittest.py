import unittest
from pack_array import pack_array


class TestSampleTests(unittest.TestCase):
    def test_should_support_example_within_description(self):
        """should support example within description"""
        self.assertEqual(pack_array([1, 2, 3, 4, 5, 6, 7, 8]), 186)
