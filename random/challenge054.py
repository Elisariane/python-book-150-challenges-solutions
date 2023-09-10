# 053 Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the
# same as the randomly selected value, display the message “You win”, otherwise display “Bad luck”. At the end, tell
# the user if the computer selected heads or tails.

import random

machine_choice = random.choice(['h', 't'])
your_choice = input("Heads or tails? Typing 'h' for head and 't' for tails \n")

if machine_choice == your_choice:
    print("You win")
else:
    print("Bad luck")
print("The machine chose", machine_choice)
