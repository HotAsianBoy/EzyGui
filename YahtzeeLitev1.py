import easygui
import random

dice = ['1', '2', '3', '4', '5', '6']
rolled = []
rolls = 0

play = easygui.buttonbox('Do you want to play Yahtzee?',
                         'play?', choices=('Yes', 'No'))
if play == 'Yes':
    while True:
        rolled = []
        for i in range(5):
            roll = random.choice(dice)
            rolled.append(roll)
        rolls += 1
        play_again = easygui.buttonbox(f'You rolled {rolled}\n'
                                       f'Would you like to roll again or stick?', title='Rolled',
                                       choices=('Roll again', 'Stick'))
        if rolls == 3:
            easygui.msgbox("Sorry, you've finished your three total rolls!")
            break

        elif play_again == 'Stick':
            break

        else:
            continue

    rolled.sort()
    if rolled[0] == rolled[4]:
        result = 'Yahtzee! You got 50 points!'
    elif rolled[0] == rolled[3] or rolled[1] == rolled[4]:
        result = 'Four of a kind! You got 30 points!'
    elif rolled[0] == rolled[2] or rolled[1] == rolled[3] or rolled[2] == \
            rolled[4]:
        result = 'Three of a kind! You got 10 points!'
    else:
        result = 'No points unfortunately! Better luck next time!'
    easygui.msgbox(f'{rolled}\n'
                   f'{result}')
else:
    easygui.msgbox("Goodbye!")