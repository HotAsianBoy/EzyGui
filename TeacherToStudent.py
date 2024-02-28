
import easygui

while True:
    school = easygui.enterbox("What School are you from? \n",
                              title="School Name")
    maximum = easygui.integerbox(f"Welcome to {school}! What is the Max amount of Children per "
                                 "Class? "
                                 "Must be between 10 and 30 \n",
                                 title="Maximum Class Size",
                                 lowerbound=10, upperbound=30)
    school_roll = easygui.integerbox(f"What is the total number of children "
                                     f"at {school}:",
                                     "Maximum amount of children",
                                     lowerbound=10, upperbound=1400)
    average = school_roll / maximum if maximum != 0 else 0
    amount_of_teachers = school_roll // average

    easygui.msgbox(f"The max amount of students per class allowed is {average}")

    teachers = easygui.integerbox("How Many Teachers are there? "
                                  "Must be between 1 and 120 \n",
                                  title="Teachers",
                                  lowerbound=1, upperbound=120)

    if teachers < amount_of_teachers:
        easygui.msgbox("You do not have enough teachers")
    else:
        easygui.msgbox("You have enough teachers")

    perform_calculation = easygui.buttonbox(f"Do you want to perform another "
                                            f"calculation?",
                                            choices=["Yes", "No"])
    if perform_calculation == "No":
        print(easygui.msgbox("Goodbye!"))
        break

