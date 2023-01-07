# 023 Ask the user to type in the first line of a nursery rhyme and display the length of the string.
# Ask for a starting number and an ending number and then display just that section of the text
# (remember Python starts counting from 0 and not 1).

nursery_rhyme = input("Enter of a nursery rhyme: ")
print(len(nursery_rhyme))
start_number = int((input("Enter a start number: ")))
ending_number = int((input("Enter a ending number: ")))
print(nursery_rhyme[start_number:ending_number])
