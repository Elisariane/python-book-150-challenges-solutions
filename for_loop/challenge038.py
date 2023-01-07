# 038 Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and repeat
# this for the number of times they entered.

name = input("What's your name: ")
num = int(input("Enter a number: "))
for i in range(num):
    for j in name:
        print(j)
