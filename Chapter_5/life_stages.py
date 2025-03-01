# write an if-elif-else chain that determines a person's stage of life
# set the variable for age
# write conditions for the following: baby, toddler, kid, teenager, adult, elder

age = 16
if age < 2:
    print(f"This person is a baby.")
elif age >= 2 and age < 4:
    print(f"This person is a toddler.")
elif age >= 4 and age < 13:
    print(f"This person is a kid.")
elif age >= 13 and age < 20:
    print(f"This person is a teenager.")
elif age >= 20 and age < 65:
    print(f"This person is an adult.")
else:
    print(f"This person is an elder.")