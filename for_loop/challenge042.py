# 042 Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want
# that number included. If they do, then add the number to the total. If they do not want it included, don’t add it
# to the total. After they have entered all fivenumbers, display the total.

total = 0
for i in range(0, 5):
    num = int(input("Enter a number: "))
    choice = input("You that number included? ('y' for yes and 'n' for no)")
    if choice == 'y':
        total += num
print(total)
