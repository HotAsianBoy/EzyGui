import easygui

nz_word = easygui.enterbox("Please enter the New Zealand word", "Word to check: ")
letters = list(nz_word)
letters.remove("u")
easygui.msgbox(f"The american spelling of {nz_word} is {''.join(letters)}!",
               f"Result!")