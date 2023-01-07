# 022 Ask the user to enter their first name and surname in lower case. Change the case to title case and join
# them together. Display the finished result.

first_name = input("What's your first name in lowercase: \n")
surname = input("What's your surname in lowercase: \n")
first_name = first_name.title()
surname = surname.title()
full_name = first_name + " " + surname
print(full_name)
