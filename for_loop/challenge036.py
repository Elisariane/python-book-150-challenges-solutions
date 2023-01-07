# 036 Alter program 035 so that it will ask the user to enter their name and a number and then display their name that
#  number of times.

name = input("What's your name: ")
num = int(input("How many times you want display your name: "))
for i in range(num):
    print(name)
