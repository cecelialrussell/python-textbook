# create a list variable called bicycles and enter names of bicycles. print the list.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# print only the first item in the list.

print(bicycles[0])

# print the first item in the list in title case.

print(bicycles[0].title())

# print the second and fourth items in the list.

print(bicycles[1])
print(bicycles[3])

# print the last item in the list.

print(bicycles[-1])

# pull the first item from the list and use it in a message. print the message.

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)