# store a pizza topping in a variable
# write an if statement to indicate if the topping is not anchovies

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print(f"Hold the anchovies!")

# write multiple if statements to provide instructions for all requested toppings

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print(f"Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print(f"Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print(f"Adding extra cheese.")

print(f"Finished making your pizza.")

# write a for loop to announce each topping as it is added to the pizza

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print(f"Finished making your pizza!")

# write an if statement to let the customer know if the restaurant is out of green peppers

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print(f"Finished making your pizza!")

# start with an empty list and ask customer if they want a plain pizza when there are no toppings

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print(f"Finished making your pizza!")
else:
    print(f"Are you sure you want a plain pizza?")

# start with a list of available toppings
# check the list of requested toppings against the list of available toppings
# if the topping is not available, let the customer know

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print(f"Finished making your pizza!")