# 056 Randomly pick a whole number between 1 and 10. Ask the user to enter a number and
# keep entering numbers until they enter the number that was randomly picked.

import random

number = random.randint(1, 10)
your_number = int(input("Choose number between 1 and 10: \n"))

while your_number != number:
    print("You not find the correct number, continue trying...")
    your_number = int(input("Choose number between 1 and 10: \n"))
print("You find the correct number!")
