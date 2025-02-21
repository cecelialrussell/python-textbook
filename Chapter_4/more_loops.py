# use for loops to print each list of foods from foods.py

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('pasta')
friend_foods.append('seafood')

print(f"My favorite foods are:")
for food in my_foods:
    print(food.title())

print(f"My friend's favorite foods are:")
for food in friend_foods:
    print(food.title())