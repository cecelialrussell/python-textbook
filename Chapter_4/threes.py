# make a list of the multiples of 3 from three to thirty
# use a for loop to print the list

multiples_of_3 = []

for value in range (3, 31):
    if value % 3 == 0:
        multiples_of_3.append(value)

print(multiples_of_3)