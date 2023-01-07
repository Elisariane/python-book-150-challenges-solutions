# 025 Ask the user to enter their first name. If the length of their first name is under five characters, ask them to
# enter their surname and join them together (without a space) and display the name in upper case. If the length of the
# first name is fiveor more characters, display their first name in lower case

first_name = input("What's your name: \n")
if len(first_name) < 5:
    surname = input("What's your surname in lowercase: \n")
    name = first_name + surname
    print(name.upper())
else:
    print(first_name.lower())
