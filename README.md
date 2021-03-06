# Game of Greed labs
---
[Click here to view the codes](game_of_greed/game_of_greed.py).

## Feature Tasks and Requirements
### Implementation Notes
- Review [rules of game](https://en.wikipedia.org/wiki/Dice_10000)

- Review [game play online](http://www.playonlinedicegames.com/farkle)

### 1st lab:
- Today is all about tackling the highest risk and/or highest priority features - **scoring, dice rolling** and **banking of points**.
    - Define a **GameLogic** class.
    - Handle calculating score for dice roll
        - Add **calculate_score** static method to GameLogic class.
        - The input to **calculate_score** is a tuple of integers that represent a dice roll.
        - The output from **calculate_score** is an integer representing the roll’s score according to rules of game.
    - Handle rolling dice
        - Add **roll_dice** static method to GameLogic class.
        - The input to **roll_dice** is an integer between 1 and 6.
        - The output of **roll_dice** is a tuple with random values between 1 and 6.
        - The length of tuple must match the argument given to **roll_dice** method.
    - Handle banking points
        - Define a **Banker** class
        - Add a **shelf** instance method
            - Input to **shelf** is the amount of points (integer) to add to shelf.
            - **shelf** should temporarily store unbanked points.
        - Add a **bank** instance method
            - **bank** should add any points on the shelf to total and reset shelf to 0.
            - **bank** output should be the amount of points added to total from shelf.
        - Add a **clear_shelf** instance method
            - **clear_shelf** should remove all unbanked points.

### 2nd lab:
- Application should implement all features from previous version
- Application should simulate rolling between 1 and 6 dice
- Application should allow user to set aside dice each roll
- Application should allow “banking” current score or rolling again.
- Application should keep track of total score
- Application should keep track of current round
- Application should have automated tests to ensure proper operation

### 3rd lab:

- Application should implement features from versions 1 and 2
- Should handle when cheating occurs.
    - Or just typos.
    - E.g. roll = `[1,3,5,2]` and user selects 1, 1, 1, 1, 1, 1
- Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- Handle zilch
    - No points for round, and round is over
- Any other questions refer to game doc or the online game or ask.


### 4th lab
- Create an AI Bot to play Game of Greed
    - The only method available for use from Game class is **play**.
    - All static methods of **GameLogic** class are available.
All other interactions with game can take place ONLY via the I/O features of the game.
        - In other words, via injectable **print** and **input** functionality.
        - It is FORBIDDEN to inject a custom **roller** function into Game class.
- Your Bot class should be added to **player_bot.py** file with name of your choosing.
- User should be able to see your bot play by executing **player_bot.py** from terminal.
- Application should implement features from previous classes


## Contributors:
___
Iris, Chen, Jesse and Corey D.

No license required


