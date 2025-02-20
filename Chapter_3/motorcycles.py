# create a list of motorcycles and print the list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change the value of the first item in the list

motorcycles[0] = 'ducati'
print(motorcycles)

# update the first item in the list back to its original value

motorcycles[0] = 'honda'
print(motorcycles)

# add ducati to the end of the list

motorcycles.append('ducati')
print(motorcycles)

# delete the last item in the list

del motorcycles[-1]
print(motorcycles)

# insert ducati at the beginning of the list

motorcycles.insert(0, 'ducati')
print(motorcycles)

# delete the first item from the list

del motorcycles[0]
print(motorcycles)

# create a variable called popped_motorcycle and use the pop method to remove the last item from the list.
# print the new list and the value of the popped variable

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# append list with previously popped variable

motorcycles.append('suzuki')
print(motorcycles)

# create a variable called last_owned with a value of the last item in the list.
# print a statement about the last motorcycle you owned.

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# append list with previously popped item

motorcycles.append('suzuki')
print(motorcycles)

# create a variable called first_owned with a value of the first item in the list.
# print a statement about the first motorcycle you owned.

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# insert the previously popped item at the beginning of the list

motorcycles.insert(0, 'honda')
print(motorcycles)

# add ducati to the end of the list

motorcycles.append('ducati')
print(motorcycles)

# remove ducati from the end of the list

motorcycles.remove('ducati')
print(motorcycles)

# add ducati to the end of the list

motorcycles.append('ducati')
print(motorcycles)

# create a variable called too_expensive and list the value as ducati.
# use the remove function in conjunction with the variable.
# print a statement why you removed it from the list.

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")
