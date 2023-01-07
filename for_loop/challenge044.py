# 044 Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and
# after each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message
# “Too many people”.

num = int(input("How many people you wants to invite to a party? "))
if num < 10:
    for i in range(0, num):
        name = input("What's name of invited? ")
        print(name + "has been invited")
else:
    print("Too many people")
