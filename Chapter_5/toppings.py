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