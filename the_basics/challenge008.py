# 008 Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by
# the number of diners and show how much each person must pay.

total_bill = float(input("Enter the  total bill value? \n"))
total_people = int(input("How many people will pay? \n"))
total_value_for_each = total_bill/total_people
print("The value was", total_value_for_each, "for each")

