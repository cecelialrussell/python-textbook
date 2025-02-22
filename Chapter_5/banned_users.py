# create a list of banned users
# create a variable called user and enter a name not in the list
# create an if statement to see if user is not in list and print statement

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")