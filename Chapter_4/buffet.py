# store five basic buffet foods in a tuple

buffet_items = ('salad', 'rolls', 'fried chicken', 'mashed potatoes', 'corn')

# use a for loop to print each item the buffet offers

for item in buffet_items:
    print(item)

# the restaurant changed its menu
# update the buffet_items tuple and use a for loop to print the new list

print(f"Monday's buffet includes:")
for item in buffet_items:
    print(item)

buffet_items = ('salad', 'rolls', 'roast beef', 'mashed potatoes', 'green beans')
print(f"Tuesday's buffet includes:")
for item in buffet_items:
    print(item)