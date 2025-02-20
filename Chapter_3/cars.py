# create a list of cars, sort them, and print the list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort the list in descending order

cars.sort(reverse=True)
print(cars)

# change the list value to original
# create print statements for original list, sorted list, and original list again

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("Here is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)

# print the list in reverse order

print(cars)
cars.reverse()
print(cars)

# find the length of the list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))