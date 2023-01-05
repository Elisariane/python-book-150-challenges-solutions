# 006 Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a user-friendly format.

start_num = int(input("What was the number of slices when you started eating "))
end_num = int(input("How many slices of pizza did you eat? "))
remaining_pieces = start_num - end_num
print("You have ", remaining_pieces, " pieces of pizza left")
