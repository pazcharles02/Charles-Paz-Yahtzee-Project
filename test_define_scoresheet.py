from unittest import TestCase
from yahtzee import define_scoresheet


class TestDefineScoresheet(TestCase):
    def test_define_scoresheet(self):
        expected = tuple([{"Aces": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                           "Three of a Kind": -1, "Four of a Kind": -1, "Full House": -1, "Small Straight": -1,
                           "Large Straight": -1, "Yahtzee": -1, "Chance": -1, "Player": 1},
                          {"Aces": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                           "Three of a Kind": -1, "Four of a Kind": -1, "Full House": -1, "Small Straight": -1,
                           "Large Straight": -1, "Yahtzee": -1, "Chance": -1, "Player": 2}])
        actual = define_scoresheet()
        self.assertEqual(expected, actual)
