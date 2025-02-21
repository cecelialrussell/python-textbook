# use the list of pizzas from the file pizzas.py
# create a list called friend_pizzas that copies the original list

my_pizzas = ['sausage', 'pepperoni', 'chicken alfredo']
friend_pizzas = my_pizzas[:]

# add a new pizza to the original list
# add a different pizza to the friend list
# print a message for each list to make sure a new pizza is stored in each list

my_pizzas.append('cheese')
friend_pizzas.append('mushroom')

print(f"My favorite pizzas are:")
print(my_pizzas)

print(f"My friend's favorite pizzas are:")
print(friend_pizzas)