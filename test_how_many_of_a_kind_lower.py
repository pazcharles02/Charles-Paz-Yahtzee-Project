from unittest import TestCase
from yahtzee import how_many_of_a_kind_lower


class TestHowManyOfAKind(TestCase):
    def test_how_many_of_a_kind_lower_1_of_a_kind(self):
        actual = how_many_of_a_kind_lower([1, 2, 3, 4, 5])
        expected = 0
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_lower_one_2_of_a_kind(self):
        actual = how_many_of_a_kind_lower([1, 1, 3, 4, 5])
        expected = 0
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_lower_two_2_of_a_kind(self):
        actual = how_many_of_a_kind_lower([1, 1, 3, 3, 5])
        expected = 0
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_lower_3_of_a_kind_3_unique_elements(self):
        actual = how_many_of_a_kind_lower([1, 1, 1, 4, 5])
        expected = 3
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_lower_3_of_a_kind_2_unique_elements(self):
        actual = how_many_of_a_kind_lower([1, 1, 1, 4, 4])
        expected = 3
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_lower_4_of_a_kind(self):
        actual = how_many_of_a_kind_lower([1, 1, 1, 1, 5])
        expected = 4
        self.assertEqual(expected, actual)

    def test_how_many_of_a_kind_lower_5_of_a_kind(self):
        actual = how_many_of_a_kind_lower([1, 1, 1, 1, 1])
        expected = 5
        self.assertEqual(expected, actual)
