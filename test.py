import easygui


name = easygui.enterbox("Hi, what is your name?")
print(name)

age = easygui.integerbox("Hi, what is your age?")
carry_on = easygui.buttonbox("Do you want to continue?",
                             choices=["Yes", "No", "Dont care!"],
                             title="Continue")


last_name = easygui.buttonbox("Choose Gender", "Gender", ["Male", "Female", "Other",])


