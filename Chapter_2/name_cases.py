# Personal Message - use a variable to represent a person's name and print a message to that person

name = "bryan"
print(f"Hello, {name.title()}!")

# Name Cases - use a variable to represent a person's name and then print the name in lowercase, uppercase, and title case

name = "cecelia"
print(name.lower())
print(name.upper())
print(name.title())

# Famous Quote - find a quote from a famous person you admire. print the quote and the name of its author.

famous_person = "lewis carroll"
quote = "One of the deep secrets of life is that all that is really worth doing is what we do for others."
print(f'{famous_person.title()} once said, "{quote}"')

# Stripping Names - use a variable to represent a person's name and include some whitespace characters at the beginning and end. 
# print the name once so whitespace is displayed, then use the stripping functions.

famous_person2 = " dolly parton "
print(famous_person2)
print(famous_person2.rstrip())
print(famous_person2.lstrip())
print(famous_person2.strip())

# File Extensions - assign the value python_notes.txt to a variable called file_name then remove the suffix

file_name = "python_notes.txt"
print(file_name.removesuffix('.txt'))