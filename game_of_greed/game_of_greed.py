from random import randint
from collections import Counter

class GameLogic:
    # def __init__(self):
    #     pass


    @staticmethod
    def calculate_score(set_dice):
        score = 0

        # ctr = Counter(set_dice)
        # print(ctr.most_common())
        # check for 3pl sets

        ctr = Counter(set_dice)
        ctr.most_common()
        if ctr[1] == 3 : return 1000
        # we need to find all triples diferent than 1, and multiply that number by 100. EXCEPT NUMBER 1
        print('ctr',  ctr)
        for i in range(2,7):
            if ctr[i] == 3 :
                pass
                # print('the 3ple is', ctr[i])
                # score += ctr[i] * 100



        # for item in set_dice:
        #     if item == 1 : score += 100
        #     if item == 5 : score += 50

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



# if __name__ == "__main__":
    gm = GameLogic()
    set_dice = (2,2,2,3,3,3)
    print('original set:', set_dice)
    result = gm.calculate_score(set_dice)
    # print(set_dice)
    # print( result)


