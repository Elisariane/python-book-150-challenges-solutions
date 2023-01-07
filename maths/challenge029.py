# 029 Ask the user to enter an integer that is over 500. Work out the square root of that number and display
# it to twodecimal places.
import math

number = int(input("Enter an integer that is over 500: "))
square_root = math.sqrt(number)
print(round(square_root, 2))
