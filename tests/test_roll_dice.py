from game_of_greed import __version__
from game_of_greed.game_of_greed import GameLogic

def test_version():
    assert __version__ == '0.1.0'


################# Roll Dice Tests ################
def test_roll_one_dice():
    actual = len(GameLogic().roll_dice(1))
    result = GameLogic().roll_dice(1)
    expected = 1
    range =True
    for i in result:
        if i > 6 or i <1:
            range= False
    assert actual == expected
    assert (range == True),'The value of the dice is not between 1 to 6'


def test_roll_three_dice():
    actual = len(GameLogic().roll_dice(3))
    result = GameLogic().roll_dice(3)
    expected = 3
    range =True
    for i in result:
        if i > 6 or i <1:
            range= False
    assert actual == expected
    assert (range == True),'The value of the dice is not between 1 to 6'
