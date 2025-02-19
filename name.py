# create a string variable for name and print in title case

name = "ada lovelace"
print(name.title())

# print the name variable in upper case and lower case

print(name.upper())
print(name.lower())

# create variables for first name and last name and then use both inside full name variable

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# create a greeting using the full_name variable

print(f"Hello, {full_name.title()}!")

# create a message variable and then print the message

message = f"Hello, {full_name.title()}!"
print(message)