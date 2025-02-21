# create a list called players and print the first three elements by slicing the list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# print the second, third, and fourth items in the list

print(players[1:4])

# omit the first index in the slice

print(players[:4])

# omit the last index in the slice

print(players[2:])

# use a negative index to output the last three players in the list

print(players[-3:])

# loop through the first three players in the list and print as part of a simple roster

print(f"Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())