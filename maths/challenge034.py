# 034 Display the following message: If the user enters 1, then it should ask them for the length of one of its sides
# and display the area. If they select 2, it should ask for the base and height of the triangle and display the area.
# If they type in anything else, it should give them a suitable error message.

print("1) Square \n2) Triangle")
choice = int(input("Enter a number: "))

if choice == 1:
    side = int(input("Enter the length of one side: "))
    area = side*2
    print(area)
elif choice == 2:
    base = int(input("Enter the number of base of the triangle: "))
    height = int(input("Enter the number of height of the triangle: "))
    area = (base*height)/2
    print(area)
else:
    print("Error message")
