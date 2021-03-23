import io
from unittest import TestCase
from unittest.mock import patch
from yahtzee import print_scoresheet


class TestPrintScoresheet(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scoresheet(self, mock_output):
        print_scoresheet(scoresheet=tuple([{"Aces": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                            "Three of a Kind": -1, "Four of a Kind": -1, "Full House": -1,
                                            "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1,
                                            "Player": 1},
                                           {"Aces": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                            "Three of a Kind": -1, "Four of a Kind": -1, "Full House": -1,
                                            "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1, "Chance": -1,
                                            "Player": 2}]))
        expected = "This is the current score!\n\n\nPlayer One's Scores\n\nAces:\t\t\t\tNot filled\nTwos:\t\t\t\tNot " \
                   "filled\nThrees:\t\t\t\tNot filled\nFours:\t\t\t\tNot filled\nFives:\t\t\t\tNot filled\nSixes:\t\t" \
                   "\t\tNot filled\nThree of a Kind:\tNot filled\nFour of a Kind:\t\tNot filled\nFull House:\t\t\tNot "\
                   "filled\nSmall Straight:\t\tNot filled\nLarge Straight:\t\tNot filled\nYahtzee:\t\t\tNot filled\n" \
                   "Chance:\t\t\t\tNot filled\n\nPlayer Two's Scores\n\nAces:\t\t\t\tNot filled\nTwos:\t\t\t\tNot " \
                   "filled\nThrees:\t\t\t\tNot filled\nFours:\t\t\t\tNot filled\nFives:\t\t\t\tNot filled\nSixes:\t\t" \
                   "\t\tNot filled\nThree of a Kind:\tNot filled\nFour of a Kind:\t\tNot filled\nFull House:\t\t\tNot "\
                   "filled\nSmall Straight:\t\tNot filled\nLarge Straight:\t\tNot filled\nYahtzee:\t\t\tNot filled\n" \
                   "Chance:\t\t\t\tNot filled\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
