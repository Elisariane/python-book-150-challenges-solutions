# 021 Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space
# between and display the name and the length of whole name.

first_name = input("What's your first name: \n")
surname = input("What's your surname: \n")
full_name = first_name + " " + surname
length_name = len(full_name)
print(full_name)
print(length_name)
