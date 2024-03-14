import easygui
import random

player1 = easygui.enterbox("Please enter the name of your 1st player:")
player2 = easygui.enterbox("Please enter the name of your 2nd player:")
player_1 = 0
player_2 = 0
while True:
    for roll in range(2):
        player_1 += 1
        die1 = random.randint(1,6)
        die2 = random.randint(1, 6)
        die3 = random.randint(1, 6)
        die4 = random.randint(1, 6)
        die5 = random.randint(1, 6)
        roll_again1 = easygui.buttonbox(f"{player1}, you rolled: \n\n {die1}, {die2}, {die3}, {die4}, and {die5}\n"
                   f"Total: {die1 + die2+ die3}", f"Player {player1}"
                    f"Game result", choices=["Roll again", "Stick"])
        if roll_again1 == "Stick":
            while True:
                for roll in range(2):
                    player_2 += 1
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    die3 = random.randint(1, 6)
                    roll_again2 = easygui.buttonbox(f"{player2}, you rolled: \n\n {die1}, {die2}, {die3}, {die4}"
                                                    f", {die5}\n"
                                           f"Total: {die1 + die2 + die3}", f"Player {player2}"
                                                                    f"Game result", choices=["Roll again", "Stick"])
                    if roll_again2 == "Stick":
                        break

