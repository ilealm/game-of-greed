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
        self.score = 0
        self.banker = Banker()
        self.round = 1
        self.game = GameLogic()
        self.roller = roller

    def play(self):

        def quit():
            """function to print result when user choose to quit"""
            print(f"Total score is {self.banker.balance} points")
            print(f"Thanks for playing. You earned {self.banker.balance} points")

        def cheat_checker(user_input, dice_roll):
            """checks whether the user is cheating or not"""
            for i in user_input:
                if i in dice_roll:
                    dice_roll.remove(i)
                else:
                    return False
            return True

        print("Welcome to Game of Greed")
        responses = input("Wanna play?")
        if responses == 'n':
            print("OK. Maybe another time")
        elif responses =='y':
            """keep the game going unless we break it"""
            while True:

                print(f"Starting round {self.round}")
                print(f"Rolling {6-len(self.dice_deck)} dice...")
                if self.roller==None:
                    rolls = self.game.roll_dice(6-len(self.dice_deck))
                else:
                    rolls = self.roller
                print(",".join([str(i) for i in rolls]))
                score_check = self.game.calculate_score(rolls)
                if score_check != 0:
                    dice_to_save = input("Enter dice to keep (no spaces), or (q)uit: ")
                    if dice_to_save != 'q':
                        dice_check = [int(elem) for elem in list(dice_to_save)]
                        result_check = cheat_checker(dice_check,list(rolls))
                        while result_check == False and dice_to_save != 'q':
                            print("Cheater!!! Or possibly made a typo...")
                            print(",".join([str(i) for i in rolls]))
                            dice_to_save = input("Enter dice to keep (no spaces), or (q)uit: ")
                            if dice_to_save != 'q':
                                dice_check = [int(elem) for elem in list(dice_to_save)]
                                result_check = cheat_checker(dice_check,list(rolls))
                else:
                    quit()
                    break

                if dice_to_save == 'q':
                    quit()
                    break
                else:
                    dice_for_score =[]
                    for i in range(len(dice_to_save)):
                        self.dice_deck.append(int(dice_to_save[i]))
                        dice_for_score.append(int(dice_to_save[i]))

                    new_score = self.game.calculate_score(dice_for_score)

                    self.banker.shelf(new_score)

                    print(f"You have {self.banker.shelved} unbanked points and {6-len(self.dice_deck)} dice remaining")

                    bank_or_not = input("(r)oll again, (b)ank your points or (q)uit ")
                    if bank_or_not == 'q':
                        quit()
                        break
                    elif bank_or_not == 'r':
                        """keep rolling without banking it"""
                        score_return = self.game.calculate_score(rolls)
                        if score_return != 0:
                            self.round+=1
                            continue
                        else:
                            quit()
                            break
                    elif bank_or_not == 'b':
                        """bank the score"""
                        print(f"You banked {self.banker.shelved} points in round {self.round}")
                        self.banker.bank()

                        self.round+=1
                        print(f'Total score is {self.banker.balance} points')


if __name__ == "__main__":
    Game()
    Game().play()

