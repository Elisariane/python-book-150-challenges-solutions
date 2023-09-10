# 058 Make a maths quiz that asks five questions by randomly generating two whole numbers
# to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer. 
# If they get it right add a point to their score. At the end of the quiz, tell them 
# how many they got correct out of five.

import random

score = 0

print("***Math Quiz****")

for i in range(1, 6):
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)

    print("\nAsk {}. {} + {}".format(i, num1, num2))

    anwser =  int(input("Enter your anwser: "))

    if (num1 + num2) == anwser:
        score+=1

print("Your score is {} of 5 questions".format(score))
