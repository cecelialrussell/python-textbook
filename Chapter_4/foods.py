# create a list of favorite foods and then copy to another list using a variable

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# create print statements for each list and print each list

print(f"My favorite foods are:")
print(my_foods)

print(f"My friend's favorite foods are:")
print(friend_foods)

# add a new food to each list and then print the statements and lists again

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f"My favorite foods are:")
print(my_foods)

print(f"My friend's favorite foods are:")
print(friend_foods)