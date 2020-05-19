from random import randint
from collections import Counter

class GameLogic:

    @staticmethod
    def calculate_score(set_dice):
        score = 0
            #test socre when you got a straight
        tracker = []
        for i in Counter(set_dice):
            tracker.append(Counter(set_dice)[i])
        if tracker == [2,2,2]:
            print(tracker)
            score = 1500
            return score

        if Counter(set_dice) == Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}):
            score = 1500
            return score

        else:
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
        return self.shelved

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        # clear_shelf()
        return self.balance

    def clear_shelf(self):
        self.shelved = 0
        return(self.shelved)



# # if __name__ == "__main__":
#     gm = GameLogic()
#     set_dice = (2,2,2,3,3,3)
#     # print('original set:', set_dice)
#     result = gm.calculate_score(set_dice)
    # print(set_dice)
    # print( result)


