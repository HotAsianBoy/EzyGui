import easygui
import random


count = 0


word = "elephant"

while count < 5:
    count += 1
    letter = random.choice()
    easygui.msgbox(f"{letter}", f"letter {count}", )