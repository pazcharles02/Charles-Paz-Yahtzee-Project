from unittest import TestCase
from yahtzee import is_small_straight


class TestIsSmallStraight(TestCase):
    def test_is_small_straight_true_with_only_small_straight(self):
        expected = True
        actual = is_small_straight([1, 2, 3, 4, 6])
        self.assertEqual(expected, actual)

    def test_is_small_straight_true_with_large_straight(self):
        expected = True
        actual = is_small_straight([1, 2, 3, 4, 5])
        self.assertEqual(expected, actual)

    def test_is_small_straight_false(self):
        expected = False
        actual = is_small_straight([1, 2, 3, 5, 6])
        self.assertEqual(expected, actual)