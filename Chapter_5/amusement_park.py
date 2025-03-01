# write an if-elif-else statement to determine the cost of an amusement park ticket

age = 12
if age < 4:
    print(f"Your admission cost is $0.")
elif age < 18:
    print(f"Your admission cost is $25.")
else:
    print(f"Your admission cost is $40.")

# write more concise code by setting a price variable in each condition

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

# add an extra elif statement to provide a senior discount

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

# omit the else block and replace with an extra elif statement

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >=65:
    price = 20

print(f"Your admission cost is ${price}.")