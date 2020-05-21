from tests.flo import Flo
from game_of_greed.game_of_greed import Game
import pytest


def test_wanna_play():
    Flo.test('tests/wanna_play.txt')


def test_wanna_play_then_quit():
    Flo.test('tests/do_wanna_play_then_quit.txt')


def test_bank_one_roll_then_quit():
    Flo.test('tests/bank_one_roll_then_quit.txt')


def test_bank_first_for_two_rounds():
    Flo.test('tests/bank_first_for_two_rounds.txt')

def test_cheat_and_fix():
    """Cheating (or typos) should not be allowed.
    Therefore the user's input must be validated
    If invalid prompt user for re-entry
    """

    Flo.test("tests/cheat_and_fix.txt")


def test_hot_dice():
    """When all dice are used without a zilch
    then user gets 6 fresh dice and continues turn.
    """
    Flo.test("tests/hot_dice.txt")



def test_zilch():
    """
    No scoring dice results in a 'zilch'
    which wipes away shelved points
    and ends turn
    """
    Flo.test("tests/zilch.txt")
