import easygui
import random


card_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
card_suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
while True:
    player = [random.choice(card_list), random.choice(card_suits)]
    computer = [random.choice(card_list), random.choice(card_suits)]
    if player == computer:
        continue
    elif card_list.index(player[0]) == card_list.index(computer[0]):
        result = "The game is a draw!"
    elif card_list.index(player[0]) > card_list.index(computer[0]):
        result = "Nice try, you lost!"
    else:
        result = "Congratulations! You won!"
    play_again = easygui.buttonbox(f"You, have the {player[0]} of"
                                    f" {player[1]},\n and I have the "
                                    f"{computer[0]} of {computer[1]}!\n\n"
                                    f"***{result}***\n\n"
                                    f"Do you want to play again?",
                                    "Game result", choices=["Yes","No"])

    if play_again == "No":
        easygui.msgbox("Thank you for playing! Have a good day!")
        break



