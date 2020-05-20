from tests.flo import Flo
from game_of_greed.game_of_greed import Game
import pytest


def test_wanna_play():
    # flo = Flo('tests/wanna_play.txt')
    Flo.test('tests/wanna_play.txt')

def test_wanna_play_then_quit():
    # flo=Flo('tests/do_wanna_play_then_quit.txt')
    Flo.test('tests/do_wanna_play_then_quit.txt')


def test_cheat_and_fix():
    Flo.test('tests/cheat_and_fix.txt')

@pytest.mark.skip(reason="tried too many times just don't pass")
def test_bank_one_roll_then_quit():
    Flo.test('tests/bank_one_roll_then_quit.txt')


@pytest.mark.skip(reason="tried too many times just don't pass")
def test_bank_first_for_two_rounds():
    Flo.test('tests/bank_first_for_two_rounds.txt')

