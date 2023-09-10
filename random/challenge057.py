# 057 Update program 056 so that it tells the user if they are too high or too low before they
# pick again.

import random

number = random.randint(1, 10)
your_number = int(input("Choose number between 1 and 10: \n"))

while your_number != number:
    print("You not find the correct number, continue trying...")
    if your_number > number:
        print("Too high")
    else:
        print("Too low")
    your_number = int(input("Choose number between 1 and 10: \n"))
print("You find the correct number!")
