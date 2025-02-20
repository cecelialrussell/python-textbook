# think of something you could sort in a list and create the list
# use every function in chapter 3

clothing = ['shirt', 'pants', 'skirt', 'socks', 'shoes', 'coat', 'underwear']
print(clothing)

# print items at specific indices

print(clothing[0])
print(clothing[3])
print(clothing[5])
print(clothing[-1])

# use an individual value in the list in a statement

message = f"I would like a new {clothing[5]}."
print(message)

message = f"{clothing[3].title()} are good for keeping feet warm."
print(message)

# modify an element in the list

clothing[0] = 'sweater'
print(clothing)

# add an element to the list using append

print(clothing)
clothing.append('shirt')
print(clothing)

# insert an element into the list

clothing.insert(3, 'dress')
print(clothing)

# delete the first item in the list

del clothing[0]
print(clothing)

# create a variable to store a popped item and use it in a statement

print(clothing)
popped_clothing = clothing.pop(2)
print(popped_clothing)
print(f"I don't want to wear a {popped_clothing}.")

# remove an item from the list

print(clothing)
clothing.remove('coat')
print(clothing)

# create a variable for an item you wish to donate and print a statement

donated_item = 'shirt'
clothing.remove(donated_item)
print(clothing)
print(f"I donated a {donated_item} to flood relief.")

# sort the list in alphabetical order

print(clothing)
clothing.sort()
print(clothing)

# print the list in reverse-alphabetical order

print(clothing)
clothing.sort(reverse=True)
print(clothing)

# print the list in reverse order

print(clothing)
clothing.reverse()
print(clothing)

# find the length of the list

print(len(clothing))