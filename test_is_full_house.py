from unittest import TestCase
from yahtzee import is_full_house


class TestIsFullHouse(TestCase):
    def test_is_full_house_true(self):
        expected = True
        actual = is_full_house([2, 2, 2, 3, 3])
        self.assertEqual(expected, actual)

    def test_is_full_house_false(self):
        expected = False
        actual = is_full_house([1, 2, 2, 3, 3])
        self.assertEqual(expected, actual)
