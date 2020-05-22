""""
Create a Game of Greed Player Bots
ONLY use public methods
- Game class constructor and play method
- DO NOT INJECT CUSTOM ROLL FUNCTION
- GameLogic, all methods available
"""
import sys
sys.path.append("~/Library/Mobile\ Documents/com~apple~CloudDocs/SCHOOL/Code_Fellows/401/python/game-of-greed/game_of_greed/")

import builtins
import re

from game_of_greed import Game
from game_of_greed import GameLogic


class BasePlayer:
    def __init__(self):
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    def _mock_print(self, *args, **kwargs):
        self.old_print(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        return self.old_input(*args, **kwargs)

    @classmethod
    def play(cls, num_games=1):

        mega_total = 0

        for i in range(num_games):
            player = cls()

            game = Game()
            game.play()
            mega_total += player.total_score
            player.reset()

        print(
            f"{num_games} games (maybe) played with average score of {mega_total // num_games}"
        )


class Naysayer(BasePlayer):
    def _mock_input(self, *args, **kwargs):
        return "n"


class NervousNellie(BasePlayer):
    """ this is the origional Nervous Nellie bot"""
    def __init__(self):
        super().__init__()
        self.roll = None

    def _mock_print(self, *args, **kwargs):
        first_arg = args[0]
        first_char = first_arg[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
        elif first_arg.startswith("Thanks for playing."):
            self.total_score = int(re.findall(r"\d+", first_arg)[0])

    def _mock_input(self, *args, **kwargs):
        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            return "y"
        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            return keepers
        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit "):
            return "b"
        else:
            raise ValueError(f"Unrecognized prompt {prompt}")


class NaughtyNellie(BasePlayer):
    """this is the new Naughty Nellie bot we build to beat Nervous Nellie"""
    def __init__(self):
        super().__init__()
        self.roll = None
        self.dice_num =0

    def _mock_print(self, *args, **kwargs):
        first_arg = args[0]

        first_char = first_arg[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
            self.dice_num = len(self.roll)
        elif first_arg.startswith("Thanks for playing."):
            self.total_score = int(re.findall(r"\d+", first_arg)[0])

    def _mock_input(self, *args, **kwargs):

        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            return "y"
        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            self.dice_num -= len(scorers)
            return keepers
        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit "):
            if self.dice_num >= 4 :
                return "r"
            return "b"
        else:
            raise ValueError(f"Unrecognized prompt {prompt}")

if __name__ == "__main__":
    from textwrap import dedent

    print(dedent("""
    this is from Nervous Nellie"""))
    NervousNellie.play(20)
    print(dedent("""
    this is from Naught Nellie:"""))
    NaughtyNellie.play(20)


