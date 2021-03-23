"""
I don't see the point of testing this function multiple times because the chosen_dice list parameter is a list my other
functions make, so there will never be another significant test case, because the only thing changing between those
cases are the actual numbers in my list, not the number of numbers, or types of objects in the list
"""

from unittest import TestCase
from yahtzee import calculate_sum_of_dice


class TestCalculateSumOfDice(TestCase):
    def test_calculate_sum_of_dice(self):
        expected = 15
        actual = calculate_sum_of_dice([1, 2, 3, 4, 5])
        self.assertEqual(expected, actual)

    def test_calculate_sum_of_dice_one_duplicate(self):
        expected = 16
        actual = calculate_sum_of_dice([1, 2, 3, 5, 5])
        self.assertEqual(expected, actual)

    def test_calculate_sum_of_dice_two_duplicates(self):
        expected = 19
        actual = calculate_sum_of_dice([1, 4, 4, 5, 5])
        self.assertEqual(expected, actual)

    def test_calculate_sum_of_dice_three_of_a_kind(self):
        expected = 18
        actual = calculate_sum_of_dice([1, 2, 5, 5, 5])
        self.assertEqual(expected, actual)

    def test_calculate_sum_of_dice_three_of_a_kind_and_duplicate(self):
        expected = 23
        actual = calculate_sum_of_dice([4, 4, 5, 5, 5])
        self.assertEqual(expected, actual)

    def test_calculate_sum_of_dice_four_of_a_kind(self):
        expected = 21
        actual = calculate_sum_of_dice([1, 5, 5, 5, 5])
        self.assertEqual(expected, actual)

    def test_calculate_sum_of_dice_five_of_a_kind(self):
        expected = 25
        actual = calculate_sum_of_dice([5, 5, 5, 5, 5])
        self.assertEqual(expected, actual)