# create a list of magician names and use a for loop to print the name of each magician

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# use a for loop to print a statement including the name of each magician

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# add another statement to the loop

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

# add a thank you message for all magicians after the for loop

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

print(f"Thank you, everyone. That was a great magic show!")