# 055 Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess
# correctly, display the message “Well done”,otherwise tell them if they are too high 
# or too low and ask them to pick a second number. If they guess correctly on their
# second guess, display “Correct”, otherwise display “You lose”.

import random


number = random.randint(1, 5)
your_number = int(input("Chosse number between 1 and 5 \n"))

if number == your_number:
    print("Well done")
else:
    if your_number > number:
        print("Too high")
    else:
        print("Too low")
    your_number = int(input("You have a second chance... Enter the number between 1 and 5 \n"))
    if number == your_number:
        print("Correct")
    else:
        print("You lose")