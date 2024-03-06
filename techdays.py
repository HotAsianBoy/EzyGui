import easygui

used_tech = easygui.enterbox(msg="Please enter tech days. Put a space between each.")
days = len(used_tech.split())
if days <= 3:
   easygui.msgbox(f"Congrats! you were on target ({days} days)")
else:
   easygui.msgbox(msg=F"What a bozo! You used tech for {days}days.")