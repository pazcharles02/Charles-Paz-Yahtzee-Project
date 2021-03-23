"""
COMP - 1510 Final Exam Functions (Yahtzee Game)
By: Charles Paz
Set: E - CST
Date: 12/05/2020
"""

import doctest
import random


def MAXIMUM_AMOUNT_OF_DICE():
    """The Maximum amount of dice that can be in one's hand (list structure)

    :postcondition: will always return 5
    :return: the integer 5
    """
    return 5


def MAXIMUM_NUMBER_TO_HAVE_AT_LEAST_3_OF_A_KIND():
    """The Maximum number of unique dice that can be in one's hand (list structure)

    :postcondition: will always return 3
    :return: the integer 3
    """
    return 3


def INVALID_SCORE_FOR_YAHTZEE_BONUS():
    """The number 0 is what is placed into the Yahtzee score and makes it invalid for any bonus

    :postcondition: will always return 0
    :return: the integer 0
    """
    return 0


def DEFAULT_SCORE_VALUE():
    """The number -1 is what is placed into all score types to serve as placeholders

    :postcondition: will always return -1
    :return: the integer -1
    """
    return -1


def MAXIMUM_AMOUNT_OF_TABS_IN_FORMATTED_PRINT():
    """The Maximum amount of tab escape characters that should be in that line of string

    The largest string among the keys of the dictionary of player scoresheets is "Large Straight" which is 14
    characters. When adding the ": ", the total is 16 characters, so one tab after that entire string becomes 20
    characters. To format everything else to look the same as this one longest string would look, I use this variable
    and calculation in the main function to ensure all the numbers of each key are printed after 20 characters,
    whitespace or not.

    :postcondition: will always return 5
    :return: the integer 5
    """
    return 5


def LENGTH_OF_TAB():
    """The length of characters in one tab escape character (list structure)

    :postcondition: will always return 4
    :return: the integer 4
    """
    return 4


def play_yahtzee() -> None:
    """Function that will be called in main to play the yahtzee game

    # I don't know if this will return anything yet. Judging from books, I think it will not return anything
    """
    scoresheet = define_scoresheet()
    while True:
        if is_player_scoresheet_full(scoresheet, 1) is False:
            print("It is Player One's turn!")
            list_of_dice = roll_dice([])
            print_out_dice(list_of_dice)
            update_scoresheet(scoresheet[0], list_of_dice)
            print_scoresheet(scoresheet)
        if is_player_scoresheet_full(scoresheet, 2) is False:
            print("It is Player Two's turn!")
            list_of_dice = roll_dice([])
            print_out_dice(list_of_dice)
            update_scoresheet(scoresheet[1], list_of_dice)
            print_scoresheet(scoresheet)
        else:
            winner = check_winner(scoresheet)
            if winner != "Draw":
                print(f"\nThe winner is {winner}!!! Congratulations!")
                break
            else:
                print("It is a draw! You both lose! >:)")
                break


def check_winner(scoresheet: tuple):
    """Check which of the two dictionaries in scoresheet has the higher sum to see who the winner is

    :param scoresheet: tuple of two dictionaries, representing the scoresheet of each player
    :return: string representing who the winner is
    >>> sample_scoresheet = ({"score": 117, "other_score": 3}, {"score": 107, "other_score": 3})
    >>> check_winner(sample_scoresheet)
    'Player One'
    >>> sample_scoresheet = ({"score": 107, "other_score": 3}, {"score": 117, "other_score": 3})
    >>> check_winner(sample_scoresheet)
    'Player Two'
    >>> sample_scoresheet = ({"score": 117, "other_score": 3}, {"score": 117, "other_score": 3})
    >>> check_winner(sample_scoresheet)
    'Draw'
    """
    list_of_score_types = [score_type for score_type in scoresheet[0]]
    total_score_of_player_one = 0
    for score_type in list_of_score_types:
        total_score_of_player_one += scoresheet[0][score_type]
    total_score_of_player_two = 0
    for score_type in list_of_score_types:
        total_score_of_player_two += scoresheet[1][score_type]
    if total_score_of_player_one > total_score_of_player_two:
        winner = "Player One"
    elif total_score_of_player_two > total_score_of_player_one:
        winner = "Player Two"
    else:
        winner = "Draw"
    return winner


def is_player_scoresheet_full(scoresheet: tuple, player_number: int) -> bool:
    """Check if the players still have turns by checking if scoresheets are completely filled

    :param scoresheet: tuple of two dictionaries, representing the scoresheet of each player
    :param player_number: the number of the player whose turn it is currently
    :return: a boolean based on if scoresheet is full or not
    >>> sample_scoresheet = ({"score": -1, "other_score": -1, "Player": 1}, {"score": 117, "other_score": -1, "Player":\
     -1})
    >>> is_player_scoresheet_full(sample_scoresheet, 1)
    False
    >>> sample_scoresheet = ({"score": -1, "other_score": -1, "Player": 1}, {"score": 117, "other_score": 3, "Player":\
     2})
    >>> is_player_scoresheet_full(sample_scoresheet, 1)
    False
    >>> sample_scoresheet = ({"score": 117, "other_score": 3, "Player": 1}, {"score": 107, "other_score": 3, "Player":\
     2})
    >>> is_player_scoresheet_full(sample_scoresheet, 1)
    True
    >>> sample_scoresheet = ({"score": 117, "other_score": 3, "Player": 1}, {"score": -1, "other_score": -1, "Player":\
     2})
    >>> is_player_scoresheet_full(sample_scoresheet, 1)
    True
    """
    for player_dictionary in scoresheet:
        if player_dictionary["Player"] == player_number:
            list_of_score_types = list(player_dictionary)
            number_of_unfilled_spaces = 0
            for score_type in list_of_score_types:
                if player_dictionary[score_type] == -1:
                    number_of_unfilled_spaces += 1
            if number_of_unfilled_spaces > 0:
                return False
            else:
                return True


def define_scoresheet() -> tuple:
    """Create the scoresheet with all default values of 0 that the user can put their scores in

    :return: a tuple of two dictionaries, representing the scoresheet of each player
    >>> define_scoresheet()
    ({'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Three of a Kind': -1,\
 'Four of a Kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1,\
 'Player': 1}, {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Three of a Kind': -1,\
 'Four of a Kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1, 'Yahtzee': -1, 'Chance': -1,\
 'Player': 2})
    """
    return ({"Aces": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, "Three of a Kind": -1,
             "Four of a Kind": -1, "Full House": -1, "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1,
             "Chance": -1, "Player": 1},
            {"Aces": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1, "Three of a Kind": -1,
             "Four of a Kind": -1, "Full House": -1, "Small Straight": -1, "Large Straight": -1, "Yahtzee": -1,
             "Chance": -1, "Player": 2})


def print_scoresheet(scoresheet: tuple):
    """Format and print the scoresheet whenever the user requests to see it

    :param scoresheet: a tuple containing two dictionaries that hold the two players' scores
    """
    print("This is the current score!\n")
    print("\nPlayer One's Scores\n")
    for score_type in list(scoresheet[0]):
        if score_type is None:
            del scoresheet[0][score_type]
        else:
            whitespace = "\t" * (MAXIMUM_AMOUNT_OF_TABS_IN_FORMATTED_PRINT() - ((len(score_type) + 1) //
                                                                                LENGTH_OF_TAB()))
            if scoresheet[0][score_type] == -1:
                print(f"{score_type}:{whitespace}Not filled")
            elif score_type == "Player":
                pass
            else:
                print(f"{score_type}:{whitespace}{scoresheet[0][score_type]}")
    print("\nPlayer Two's Scores\n")
    for score_type in list(scoresheet[1]):
        if score_type is None:
            del scoresheet[1][score_type]
        else:
            whitespace = "\t" * (MAXIMUM_AMOUNT_OF_TABS_IN_FORMATTED_PRINT() - ((len(score_type) + 1) //
                                                                                LENGTH_OF_TAB()))
            if scoresheet[1][score_type] == -1:
                print(f"{score_type}:{whitespace}Not filled")
            elif score_type == "Player":
                pass
            else:
                print(f"{score_type}:{whitespace}{scoresheet[1][score_type]}")


def calculate_sum_of_dice(chosen_dice: list) -> int:
    """ Calculate the sum of a specific dice in a roll

    :param chosen_dice: a list of length 5 that the user has been left with to input into a score
    :precondition: chosen_dice must be a list of length 5
    :return: an integer of the sum of all the final dice values in the list
    >>> calculate_sum_of_dice([1, 2, 3, 4, 5])
    15
    >>> calculate_sum_of_dice([6, 5, 4, 3, 2])
    20
    >>> calculate_sum_of_dice([6, 6, 6, 6, 6])
    30
    """
    sum_of_dice = 0
    for die in chosen_dice:
        sum_of_dice += die
    return sum_of_dice


def update_scoresheet(player_scoresheet: dict, current_dice: list):
    """Update the dictionaries in the tuple to update the players' scoresheets

    # Does not actually return anything, just updates the value in the dictionary inside the tuple

    :param player_scoresheet: a dictionary that represents the player's scores
    :param current_dice: a list of the dice that the user holds currently
    with
    """
    input_location = ask_user_for_score_input_location(player_scoresheet)
    upper_section = ("Aces", "Twos", "Threes", "Fours", "Fives", "Sixes")
    score = 0
    if input_location in upper_section:
        score = (how_many_of_a_kind_upper(current_dice, upper_section.index(input_location) + 1)) * \
                (upper_section.index(input_location) + 1)
    elif input_location == "Three of a Kind" or "Four of a Kind" or "Yahtzee":
        score = calculate_score_for_lower_section_how_many_of_a_kind(input_location, player_scoresheet, current_dice)
    elif input_location == "Full House":
        if is_full_house(current_dice) is True:
            score = 25
    elif input_location == "Small Straight":
        if is_small_straight(current_dice) is True:
            score = 30
    elif input_location == "Large Straight":
        if is_large_straight(current_dice) is True:
            score = 40
    elif input_location == "Chance":
        score = calculate_sum_of_dice(current_dice)
    player_scoresheet[input_location] = score


def calculate_score_for_lower_section_how_many_of_a_kind(input_location, player_scoresheet: dict, current_dice: list):
    """Calculate what score should be returned if the score type is "How many of a kind" in the lower section

    :param input_location: the score type, represented as the key in the dictionary of the player scoresheet
    :param player_scoresheet: the dictionary that represents the player's scoresheet
    :param current_dice: a list containing all the dice the player currently holds
    :return: an integer that represents the score the player deserves for that score input
    >>> sample_scoresheet = {}
    >>> calculate_score_for_lower_section_how_many_of_a_kind("Three of a Kind", sample_scoresheet, [2, 2, 2, 1, 1])
    8
    >>> sample_scoresheet = {"Yahtzee": 0}
    >>> calculate_score_for_lower_section_how_many_of_a_kind("Yahtzee", sample_scoresheet, [2, 2, 2, 2, 2])
    50
    >>> sample_scoresheet = {"Yahtzee": 50}
    >>> calculate_score_for_lower_section_how_many_of_a_kind("Yahtzee", sample_scoresheet, [2, 2, 2, 2, 2])
    150

    """
    score = 0
    if input_location == "Three of a Kind":
        if how_many_of_a_kind_lower(current_dice) == 3:
            score = calculate_sum_of_dice(current_dice)
    elif input_location == "Four of a Kind":
        if how_many_of_a_kind_lower(current_dice) == 4:
            score = calculate_sum_of_dice(current_dice)
    elif input_location == "Yahtzee":
        if how_many_of_a_kind_lower(current_dice) == 5:
            score = 50
            if player_scoresheet["Yahtzee"] > 0:
                score = player_scoresheet["Yahtzee"] + 100
    return score


def ask_user_for_score_input_location(player_scoresheet: dict) -> str:
    """Find the key that the player wishes to store their score from their dice roll in

    :param player_scoresheet: a dictionary that represents the player's scores
    :return: a string representing the key that stores the value of the score the player wants to store
    """
    while True:
        list_of_score_types = list(player_scoresheet)
        valid_score_types = [score_type for score_type in list_of_score_types if player_scoresheet[score_type] == -1]
        if player_scoresheet["Yahtzee"] != INVALID_SCORE_FOR_YAHTZEE_BONUS() and player_scoresheet["Yahtzee"] != \
                DEFAULT_SCORE_VALUE():
            valid_score_types.append("Yahtzee")
        index_counter = 1
        for score_type in valid_score_types:
            print(f"{index_counter}: {score_type}")
            index_counter += 1
        try:
            input_location = int(input("Please input a number based on the numbered list for where you want to put your"
                                       " score for your dice!\n"))
            if input_location not in list(range(index_counter)):
                print(f"Please input a valid number! (A number in between 1 and {index_counter - 1})")
                ask_user_for_score_input_location(player_scoresheet)
            else:
                return valid_score_types[int(input_location) - 1]
        except ValueError:
            pass


def roll_dice(given_dice: list, rolls=2) -> list:
    """Roll a specified number of dice based on how many the user has chosen to not keep

    The function will also identify how many dice the user actually wants to keep # I might split this up into a helper
                                                                                    function, but as of right now, am
                                                                                    confident I won't

    # Planning to make this a recursive function that calls itself again with the list of kept dice as a parameter

    :param given_dice: a list of the dice that the user currently has kept
    :param rolls: an integer representing how many re-rolls the user has left
    :return: a list of all the dice that have been kept after rolling
    """
    current_dice = sorted(
        given_dice[:] + [random.randint(1, 6) for _ in range(MAXIMUM_AMOUNT_OF_DICE() - len(given_dice))])
    if rolls > 0 and len(given_dice) != MAXIMUM_AMOUNT_OF_DICE():
        removed_dice = 0
        while removed_dice < MAXIMUM_AMOUNT_OF_DICE():
            try:
                die_to_remove = int(identify_which_dice_to_keep(current_dice))
            except ValueError:
                return roll_dice(current_dice, rolls - 1)
            removed_dice += 1
            try:
                current_dice.remove(current_dice[int(die_to_remove) - 1])
            except IndexError:
                return roll_dice(current_dice, rolls - 1)
        return roll_dice(current_dice, rolls - 1)
    else:
        return current_dice


def identify_which_dice_to_keep(current_dice):
    """Find which dice to keep based on user input

    :param current_dice: a list containing all the dice the player currently holds
    """
    if len(current_dice) > 0:
        print_out_dice(current_dice)
        die_to_remove = input("Please input a number based on the number indexes listed on the left side of "
                              "each die. If you would not like to remove any more dice, input anything else\n")
        return die_to_remove
    else:
        pass


def print_out_dice(current_dice):
    """Print the dice in a specifically formatted method

    :param current_dice: a list containing all the dice the player currently holds
    """
    print("These are the dice you currently hold in hand")
    index_counter = 1
    for die in current_dice:
        print(f"   -----\n{index_counter}: | {die} |\n   -----")
        index_counter += 1


def how_many_of_a_kind_upper(chosen_dice: list, number_to_look_for: int) -> int:
    """Determine how many of a kind of dice number/roll there are in chosen dice

    :param chosen_dice: a list of dice of length 5 that the user has chosen to keep or been forced to keep after 3 turns
    :param number_to_look_for: the number we're checking for how many of a kind there are in the dice roll
    :return: an integer that represents the largest number of identical dice there are in the chosen_dice list
    >>> how_many_of_a_kind_upper([1, 2, 3, 4, 5], 1)
    1
    >>> how_many_of_a_kind_upper([2, 2, 3, 4, 5], 2)
    2
    >>> how_many_of_a_kind_upper([4, 4, 4, 4, 4], 4)
    5
    """
    return chosen_dice.count(number_to_look_for)


def how_many_of_a_kind_lower(chosen_dice: list) -> int:
    """Determine how many of a kind of dice number/roll there are in chosen dice

    :param chosen_dice: a list of dice of length 5 that the user has chosen to keep or been forced to keep after 3 turns
    :return: an integer that represents the largest number of identical dice there are in the chosen_dice list
    >>> how_many_of_a_kind_lower([1, 2, 3, 4, 5])
    0
    >>> how_many_of_a_kind_lower([5, 5, 5, 5, 5])
    5
    >>> how_many_of_a_kind_lower([3, 3, 3, 5, 5])
    3
    """
    set_of_dice = set(chosen_dice)
    if len(set_of_dice) <= MAXIMUM_NUMBER_TO_HAVE_AT_LEAST_3_OF_A_KIND():
        for die in chosen_dice:
            if chosen_dice.count(die) >= 3:
                return chosen_dice.count(die)
    return 0


def is_full_house(chosen_dice: list) -> bool:
    """Determine if the roll is a full house

    :param chosen_dice: a list of dice of length 5 that the user has chosen to keep or been forced to keep after 3 turns
    :precondition: numbers in chosen_dice must greater than 0 and less than 7
    :return: a boolean based on whether or not the chosen_dice list qualifies for a full house
    >>> is_full_house([1, 1, 1, 2, 2])
    True
    >>> is_full_house([1, 2, 3, 4, 5])
    False
    """
    if len(set(chosen_dice)) == 2:
        if chosen_dice.count(chosen_dice[0]) == 2 or 3:
            return True
    else:
        return False


def is_small_straight(chosen_dice: list) -> bool:
    """Determine if the roll is a small straight

    3 and 4 are vital numbers in a small straight because the user can only have 5 dice in a list, therefore if they
    were to get a small straight, which is 4 consecutive numbers, 3 and 4 have to be among those consecutive numbers

    :param chosen_dice: a list of dice of length 5 that the user has chosen to keep or been forced to keep after 3 turns
    :precondition: numbers in chosen_dice must greater than 0 and less than 7
    :return: a boolean based on whether or not the chosen_dice list qualifies for a small straight
    >>> is_small_straight([1, 2, 3, 4, 6])
    True
    >>> is_small_straight([2, 3, 4, 5, 5])
    True
    >>> is_small_straight([1, 3, 4, 5, 6])
    True
    >>> is_small_straight([2, 3, 3, 5, 5])
    False
    """
    if len(set(chosen_dice)) >= 4 and 4 in chosen_dice and 3 in chosen_dice:
        number_of_times_next_number_minus_current_number_equals_one = 0
        current_hand = sorted(list(set(chosen_dice)))
        index_counter = 1
        for die in current_hand:
            try:
                if (die + 1) == current_hand[index_counter]:
                    number_of_times_next_number_minus_current_number_equals_one += 1
                index_counter += 1
            except IndexError:
                return number_of_times_next_number_minus_current_number_equals_one >= 3
    else:
        return False


def is_large_straight(chosen_dice: list) -> bool:
    """Determine if the roll is a long straight

    :param chosen_dice: a list of dice of length 5 that the user has chosen to keep or been forced to keep after 3 turns
    :return: a boolean based on whether or not the chosen_dice list qualifies for a long straight
    >>> is_large_straight([1, 2, 3, 4, 5])
    True
    >>> is_large_straight([2, 3, 4, 5, 6])
    True
    >>> is_large_straight([1, 2, 3, 4, 6])
    False
    >>> is_large_straight([2, 3, 3, 5, 5])
    False
    """
    if len(set(chosen_dice)) == 5:
        if 1 in chosen_dice and 6 not in chosen_dice:
            return True
        elif 6 in chosen_dice and 1 not in chosen_dice:
            return True
        else:
            return False
    else:
        return False


def main():
    doctest.testmod()
    play_yahtzee()


if __name__ == "__main__":
    main()
