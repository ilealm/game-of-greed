from tests.flo import Flo
from game_of_greed.game_of_greed import Game
import pytest


def test_wanna_play():
    Flo.test('tests/wanna_play.txt')


def test_wanna_play_then_quit():
    Flo.test('tests/do_wanna_play_then_quit.txt')


def test_cheat_and_fix():
    Flo.test('tests/cheat_and_fix.txt')


def test_bank_one_roll_then_quit():
    Flo.test('tests/bank_one_roll_then_quit.txt')


def test_bank_first_for_two_rounds():
    Flo.test('tests/bank_first_for_two_rounds.txt')

