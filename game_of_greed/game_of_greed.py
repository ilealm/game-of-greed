from random import randint
from collections import Counter


class GameLogic:

    @staticmethod
    def calculate_score(set_dice):
        score = 0
        """testing whether you get 3 pairs"""
        tracker = []
        for i in Counter(set_dice):
            tracker.append(Counter(set_dice)[i])
        if tracker == [2,2,2]:
            score = 1500
            return score
        """check whether you got a straight"""
        if Counter(set_dice) == Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}):
            score = 1500
            return score
        else:
            """calculate all other combo for scoring"""
            if Counter(set_dice)[1]:
                if Counter(set_dice)[1]<=2:
                    addition = 100*Counter(set_dice)[1]
                    score += addition
                elif Counter(set_dice)[1] >=3:
                    addition = 100*10*(Counter(set_dice)[1]-2)
                    score += addition
            if Counter(set_dice)[5]:
                if Counter(set_dice)[5]<=2:
                    addition = 50*Counter(set_dice)[5]
                    score += addition
                elif Counter(set_dice)[5] >=3:
                    addition = 50*10*(Counter(set_dice)[5]-2)
                    score += addition
            for i in [2,3,4,6]:
                if Counter(set_dice)[i]>=3:
                    addition = i*100*(Counter(set_dice)[i]-2)
                    score+=addition
        return score

    @staticmethod
    def roll_dice(num_dices):
        num_dices_tuple = []
        for i in range(num_dices):
            num_dices_tuple.append(randint(1,6))
        return tuple(num_dices_tuple)


    @staticmethod
    def get_scorers(dice):
        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        for i in range(len(dice)):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(dice[i])

        return tuple(scorers)


class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0


    def shelf(self, points_to_add):
        self.shelved += points_to_add


    def bank(self):
        self.balance += self.shelved
        self.shelved = 0


    def clear_shelf(self):
        self.shelved = 0


class Game:
    def __init__(self, roller=None):
        self.dice_deck = []
        self.banker = Banker()
        self.round = 1
        self.game = GameLogic()
        self.roller = roller

    def quit_game(self):
            """function to print result when user choose to quit"""
            print(f"Total score is {self.banker.balance} points")
            print(f"Thanks for playing. You earned {self.banker.balance} points")

    @staticmethod
    def cheat_checker(user_input, dice_roll):
            """checks whether the user is cheating or not"""
            for i in user_input:
                if i in dice_roll:
                    dice_roll.remove(i)
                else:
                    return False
            return True

    def greeting(self):
        """ask whether the user want to play the game"""
        print("Welcome to Game of Greed")
        responses = input("Wanna play?").lower()
        if responses == 'n' or responses == 'no':
            print("OK. Maybe another time")
        elif responses == 'y' or responses == 'yes':
            self.game_cycle()
        else:
            print("Not a good response, please enter either y or n")
            self.greeting()


    def show_shelf_score(self,user_choice):
        """display the scores on shelf and print to console"""
        dice_for_score =[]
        for i in range(len(user_choice)):
            self.dice_deck.append(int(user_choice[i]))
            dice_for_score.append(int(user_choice[i]))

        new_score = self.game.calculate_score(dice_for_score)

        self.banker.shelf(new_score)

        print(f"You have {self.banker.shelved} unbanked points and {6-len(self.dice_deck)} dice remaining")

        return

    def hot_hand_checker(self, dice_check):
        """function to check whether user is hitting a hot hand"""
        score = self.game.calculate_score(dice_check)
        checker = True
        for i in dice_check:
            new_list = dice_check.copy()
            new_list.remove(i)
            new_score = self.game.calculate_score(new_list)
            if new_score == score:
                checker = False
        return checker



    def game_cycle(self):
        bank_checker = False
        while self.round <= 20:

            if bank_checker == False:
                print(f"Starting round {self.round}")

            print(f"Rolling {6-len(self.dice_deck)} dice...")
            if self.roller==None:
                rolls = self.game.roll_dice(6-len(self.dice_deck))
            else:
                rolls = self.roller(6-len(self.dice_deck))
                # rolls = self.roller
            if len(rolls) != 0:
                print(",".join([str(i) for i in rolls]))
            score_check = self.game.calculate_score(rolls)
            if score_check == 0:
                print("Zilch!!! Round over")
                # self.quit_game()
                print(f"You banked {self.banker.balance} points in round {self.round}")
                print(f'Total score is {self.banker.balance} points')
                self.dice_deck = []
                bank_checker = False
                self.round+=1
                self.banker.clear_shelf()
                continue
            else:
                dice_to_save = input("Enter dice to keep (no spaces), or (q)uit:")
                if dice_to_save == 'q':
                    return self.quit_game()
                else:
                    dice_check = [int(elem) for elem in list(dice_to_save)]
                    ## dice_check must be greater than 0 before checking if cheat
                    result_check = self.cheat_checker(dice_check,list(rolls))
                    while result_check == False:
                        print("Cheater!!! Or possibly made a typo...")
                        print(",".join([str(i) for i in rolls]))
                        dice_to_save = input("Enter dice to keep (no spaces), or (q)uit: ")
                        if dice_to_save == 'q':
                            return self.quit_game()
                        else:
                            dice_check = [int(elem) for elem in list(dice_to_save)]
                            result_check = self.cheat_checker(dice_check,list(rolls))

                    self.show_shelf_score(dice_to_save)

                    actual_score = self.game.calculate_score(rolls)


                    hot_hand = self.hot_hand_checker(dice_check)
                    hot_hand_tracker = False
                    if len(dice_to_save) == len(rolls):
                        if hot_hand == True:
                            self.dice_deck = []
                            hot_hand_tracker = True

                    bank_or_not = input("(r)oll again, (b)ank your points or (q)uit ")
                    actual_score = self.game.calculate_score(rolls)

                    if bank_or_not == 'q':
                        return self.quit_game()

                    elif bank_or_not == 'r':
                        """keep rolling without banking it"""
                        score_return = self.game.calculate_score(rolls)
                        bank_checker = True

                        if score_return != 0 and len(self.dice_deck) != 6:

                            continue
                        else:
                            self.quit_game()
                            continue
                    elif bank_or_not == 'b':
                        """bank the score"""
                        if hot_hand_tracker == True:
                            print(f"You banked {self.banker.shelved} points in round {self.round+1}")
                        else:
                            print(f"You banked {self.banker.shelved} points in round {self.round}")
                        self.banker.bank()
                        print(f'Total score is {self.banker.balance} points')
                        self.round+=1
                        self.dice_deck = []
                        bank_checker = False

        self.quit_game()

    def play(self):
        self.greeting()


if __name__ == "__main__":
    # Game()
    Game().play()
