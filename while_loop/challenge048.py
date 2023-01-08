# 048 Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has
# now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until
# they no longer want to invite anyone else to the party and then display how many people they have coming to the party.


total = 0
again = "y"
while again == "y":
    name = input("What's name of invited? ")
    print(name + " has been invited")
    again = input("Want to invite someone else? ")
    total += 1
print(total, "people come to your party")
