# 011 Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller
# number goes into the larger number in a user-friendly format.

larger = int(input("Enter a number over 100: \n"))
smaller = int(input("Enter a number under 10: \n"))
total = larger // smaller
print("Smaller number", smaller, "goes into", larger, total, "times")
