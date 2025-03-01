# make a list of five or more usernames including admin
# loop through the list and print a greeting for each user upon logging in
# if the user is admin, print a special message

user_list = ['admin', 'bryan', 'cecelia', 'linda', 'amanda']

for user in user_list:
    if user == 'admin':
        print(f"Hello admin, would you like a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

# empty the list and add a message when the list is empty

user_list = []

if user_list:
    for user in user_list:
        if user == 'admin':
            print(f"Hello admin, would you like a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print(f"We need to find some users!")

