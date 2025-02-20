# if you could invite anyone living or dead to dinner, who would you invite?
# create a list with three names.
# print a message to each person in the list inviting them to dinner.

guest_list = ['brandy thompson', 'rachel bolen', 'cecil lovely']
message = f"Dear, {guest_list[0].title()}. Please join me for dinner."
print(message)

message = f"Dear, {guest_list[1].title()}. Please join me for dinner."
print(message)

message = f"Dear, {guest_list[2].title()}. Please join me for dinner."
print(message)

# one of your guests is unable to make it.
# create a variable and remove the guest from the list.
# print a statement to indicate they are unable to make it.

negative_response = 'cecil lovely'
guest_list.remove(negative_response)
print(guest_list)
print(f"Your friend {negative_response.title()} is unable to make it to dinner.")

# invite another guest to dinner by appending the list
# print a second set of messages

guest_list.append('tessa horrighs')
message = f"Dear, {guest_list[0].title()}. Please join me for dinner."
print(message)

message = f"Dear, {guest_list[1].title()}. Please join me for dinner."
print(message)

message = f"Dear, {guest_list[2].title()}. Please join me for dinner."
print(message)

# invite three more guests to dinner

guest_list.append('jenny spears')
guest_list.insert(0, 'crystal howard')
guest_list.insert(3, 'jessica ratliff')
print(guest_list)
message = f"Dear, {guest_list[0].title()}. Please join me for dinner."
print(message)

message = f"Dear, {guest_list[1].title()}. Please join me for dinner."
print(message)

message = f"Dear, {guest_list[2].title()}. Please join me for dinner."
print(message)

message = f"Dear, {guest_list[3].title()}. Please join me for dinner."
print(message)

message = f"Dear, {guest_list[4].title()}. Please join me for dinner."
print(message)

message = f"Dear, {guest_list[5].title()}. Please join me for dinner."
print(message)

# now you only have space for two guests
# print a message saying you can only accommodate two people

print("I no longer have room for six guests. I can only invite two people.")

# use the pop function until the list is down to two people
# print a message for each guest with an apology

send_apology = guest_list.pop()
print(f"I am sorry, {send_apology.title()}. I must cancel your invitation. Maybe next time.")

send_apology = guest_list.pop()
print(f"I am sorry, {send_apology.title()}. I must cancel your invitation. Maybe next time.")

send_apology = guest_list.pop()
print(f"I am sorry, {send_apology.title()}. I must cancel your invitation. Maybe next time.")

send_apology = guest_list.pop()
print(f"I am sorry, {send_apology.title()}. I must cancel your invitation. Maybe next time.")

# print a message to the remaining guests letting them know they are still invited.

print(f"Hello, {guest_list[0].title()}. I hope you can still join me for dinner Friday night.")
print(f"Hello, {guest_list[1].title()}. I hope you can still join me for dinner Friday night.")

# delete the last two names from the list so the list is empty and then print the list to confirm.

del guest_list[0]
del guest_list[0]
print(guest_list)


