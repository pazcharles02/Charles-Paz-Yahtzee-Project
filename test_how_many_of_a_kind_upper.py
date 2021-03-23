from unittest import TestCase
from yahtzee import how_many_of_a_kind_upper


class TestHowManyOfAKind(TestCase):
    def test_how_many_of_a_kind_upper_1_of_a_kind(self):
        actual = how_many_of_a_kind_upper([1, 2, 3, 4, 5], 1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_upper_one_2_of_a_kind(self):
        actual = how_many_of_a_kind_upper([1, 1, 3, 4, 5], 1)
        expected = 2
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_upper_two_2_of_a_kind(self):
        actual = how_many_of_a_kind_upper([1, 1, 3, 3, 5], 1)
        expected = 2
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_upper_3_of_a_kind(self):
        actual = how_many_of_a_kind_upper([1, 1, 1, 4, 5], 1)
        expected = 3
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_upper_4_of_a_kind(self):
        actual = how_many_of_a_kind_upper([1, 1, 1, 1, 5], 1)
        expected = 4
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_upper_5_of_a_kind(self):
        actual = how_many_of_a_kind_upper([1, 1, 1, 1, 1], 1)
        expected = 5
        self.assertEqual(expected, actual)
