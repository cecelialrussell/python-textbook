# write a series of conditional tests
# print a statement describing each test and your prediction for the results of each test

sky = 'blue'
print(f"Is sky == 'blue' ? I predict True.")
print(sky == 'blue')

print(f"Is sky == 'green' ? I predict False.")
print(sky == 'green')

supervisor = 'linda'
print(f"Is my supervisor == 'linda' ? I predict True.")
print(supervisor == 'linda')

print(f"Is my supervisor == 'richard' ? I predict False.")
print(supervisor == 'richard')

cake = 'chocolate'
print(f"Is the cake == 'chocolate' ? I predict True.")
print(cake == 'chocolate')

print(f"Is the cake == 'vanilla' ? I predict False.")
print(cake == 'vanilla')

band = 'hammertowne'
print(f"Is the band == 'hammertowne' ? I predict True.")
print(band == 'hammertowne')

print(f"Is the band == 'balsam range' ? I predict False.")
print(band == 'balsam range')

car = 'gmc'
print(f"Is car == 'gmc' ? I predict True.")
print(car == 'gmc')

print(f"Is car == 'pontiac' ? I predict False.")
print(car == 'pontiac')

# create a string variable and write a test to check for equality

pet = 'dog'
print(f"Is your pet a cat?")
print(pet == 'cat')

# write a string variable and write a test to check for inequality

skirt = 'green'
print(f"Is your skirt a something other than the color blue?")
print(skirt != 'blue')

# write a string variable and write a test using the lower() method

my_car = 'GMC'
print(car.lower() == 'gmc')

# create a numeric variable and write a test to check for equality

age = 41
if age == 41:
    print(f"You are officially in your 40s.")

# create a numeric variable and write a test to check for inequality

age = 41
if age != 15:
    print(f"I'm sorry. You may not throw a quinceanera.")

# create a numeric variable and write a test to check if greater than a certain value

temperature = 75
if temperature > 70:
    print(f"It feels nice outside. I don't think I need a jacket.")

# create a numeric variable and write a test to check if less than a certain value

inflated_tires = 3
if inflated_tires < 4:
    print(f"I have a flat tire!")

# create a numeric variable and write a test to check if greater than or equal to a certain value

eggs = 12
if eggs >= 12:
    print(f"You have at least a dozen of eggs. Let's make deviled eggs!")

# create a numeric variable and write a test to check if less than or equal to a certain value

guests = 4
if guests <= 4:
    print(f"You have enough chairs for all the guests.")

# write a test using the and keyword

attendance = 50
if (attendance > 30) and (attendance < 75):
    print(f"There are a lot of people at this meeting.")

# write a test using the or keyword

guest_list = ['annie', 'bobby', 'carl', 'david', 'erica']
if ('erica' in guest_list) or ('bobby' in guest_list):
    print(f"We need to offer vegetarian meal options.")

# create a list and write a test to see if the item is in the list

bands = ['hammertowne', 'balsam range', 'sister sadie', 'lonesome river band']
print(f"Is Hammertowne on the concert schedule?")
print('hammertowne' in bands)

# create a list and write a test to see if the item is not in the list

bands = ['hammertowne', 'balsam range', 'sister sadie', 'lonesome river band']
print(f"Are the West Liberty Mountain Boys on the concert schedule?")
print('west liberty mountain boys' in bands)
