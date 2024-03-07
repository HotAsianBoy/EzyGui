import easygui

while True:
    places_to_visit = easygui.enterbox("Please enter the five places you would most "
                                       "like to visit!\nSeperate each"
                                       "place with a comma:  ",
                                       "Enter favourite places:")
    places = places_to_visit.split(",")
    if len(places) != 5:
        easygui.msgbox(f"Sorry, you can only enter the number of 5 places\n"
                       f"and you entered {len(places)} places!",
                       "There are too many places!")
    else:
        break

for place in places:
    output = f"\n* ".join(places)
easygui.msgbox(f"My bucket list for places in the world is: \n\n* {output}", "Travel bucket list")