# create an empty list called squares. 
# use a for loop to populate the list with the first 10 square numbers
# print the list

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# empty the list by using a for loop

while squares:
    print(f"Removing: ", squares[0])
    current_value = squares.pop(0)
    print(squares)
    print("Removed: ", current_value)
print("Yay! Squares is empty!")

# clean up the code by omitting the temporary square variable and appending each new value directly to list

for value in range(1, 11):
    squares.append(value ** 2)

print(squares)
