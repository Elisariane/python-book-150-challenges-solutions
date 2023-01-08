# 047 Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they
# want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they
# do not answer “y”. Once the loop has stopped, display the total.

total = 0
num1 = int(input("Enter a number: "))
choice = "y"
while choice == "y":
    num2 = int(input("Enter a number: "))
    total += num2
    choice = input("You want to enter another number: (y/n)")
print(total)
