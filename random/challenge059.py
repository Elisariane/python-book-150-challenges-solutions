# 059 Display five colours and ask the user to pick one. If they pick the same as the
# program has chosen, say “Well done”, otherwise display a witty answer which involves
# the correct colour, e.g. “I bet you are GREEN with envy” or “You are probably feeling
# BLUE right now”. Ask them to guess again; if they have still not got it right, keep
# giving them the same clue and ask the user to enter a colour until they guess it correctly.

import random 

colours = ["blue", "green", "yellow", "red", "white"]

correct_color = random.choice(colours)
print("Choose one of these colors blue, green, yellow, red or white")
try_again = True

while try_again:
    your_choice = input("Enter a colour: ").lower()
    if your_choice == correct_color:
        print("Well done")
        try_again = False

    else:
        if correct_color == "blue":
            print("Don't feel BLUE")
        elif correct_color == "green":
            print("I bet you're GREEN with envy")
        elif correct_color == "white":
            print("Are you WHITE as sheet, as you didn't guess correctly?")
        elif correct_color == "red":
            print("I bet you're RED with rage")
        elif correct_color == "yellow":
            print("I know that when you wake up you will give your best YELLOW smile")
