import easygui
import random


card_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
card_suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
while True:
    deck = []
    for suit in card_suits:
        for card in card_list:
            deck.append([card, suit])
    random.shuffle(deck)
    draw = []
    for card in deck[0:7]:
        draw.append(f"The card is {deck.index(card)+1}: {card[0]} of {card[1]}")
    for item in draw:
        show_cards = f"\n*".join(draw)
    draw_again = easygui.buttonbox(f"You have drawn:\n\n"
                                   f"* {show_cards}\n\n"
                                   f"Would you like to play again?","Random draw"
                                   , choices=["Yes", "No"])
    if draw_again == "No":
        break
