import easygui
import random

dice = ['1', '2', '3', '4', '5', '6']
players = ['Player 1', 'Player 2']
scores = {player: 0 for player in players}


def roll_dice():
    return [random.choice(dice) for _ in range(5)]


def get_result(rolled):
    rolled.sort()
    if rolled[0] == rolled[4]:
        return 'Yahtzee', 50
    elif rolled[0] == rolled[3] or rolled[1] == rolled[4]:
        return 'Four of a kind', 30
    elif rolled[0] == rolled[2] or rolled[1] == rolled[3] or rolled[2] == \
            rolled[4]:
        return 'Three of a kind', 10
    else:
        return 'Better luck next time', 0


play = easygui.buttonbox('Hello and Welcome! Do you want to play Yahtzee?',
                         title='Do you want to play?', choices=('Yes', 'No'))
if play == 'Yes':
    for player in players:
        rolls = 0
        while rolls < 3:
            rolled = roll_dice()
            rolls += 1
            play_again = easygui.buttonbox(
                f'{player}, you rolled {rolled}!\nWould you like to roll again or stick?', title='Rolled',
                choices=('Roll again', 'Stick'))
            if play_again == 'Stick':
                break
        result, points = get_result(rolled)
        scores[player] += points
        easygui.msgbox(
            f'{player}, you rolled {rolled}\n{result}. Your total score is {scores[player]}!')

    winner = max(scores, key=scores.get)
    easygui.msgbox(f'TCongratulations {winner}! You win with a score of {scores[winner]}!')
else:
    easygui.msgbox("Thanks for coming, Goodbye!", title='Goodbye')