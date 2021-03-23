from unittest import TestCase
from yahtzee import is_large_straight


class TestIsLongStraight(TestCase):
    def test_is_long_straight_true_one_to_five(self):
        expected = True
        actual = is_large_straight([1, 2, 3, 4, 5])
        self.assertEqual(expected, actual)

    def test_is_long_straight_true_two_to_six(self):
        expected = True
        actual = is_large_straight([2, 3, 4, 5, 6])
        self.assertEqual(expected, actual)

    def test_is_long_straight_false(self):
        expected = False
        actual = is_large_straight([1, 2, 3, 4, 6])
        self.assertEqual(expected, actual)
