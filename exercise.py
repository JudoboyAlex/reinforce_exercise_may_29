

# Display the list of available seats to your user, like so:
# Row 1 seat 1 is free.
# Row 1 seat 3 is free.
# Row 1 seat 4 is free.
# Row 2 seat 2 is free.
# Row 3 seat 3 is free.
# Row 3 seat 4 is free.

print("Row 1 seat 1 is free. Row 1 seat 3 is free. Row 1 seat 4 is free. Row 2 seat 2 is free. Row 3 seat 3 is free. Row 3 seat 4 is free.")

# For each available seat, use input() to prompt your user to choose whether they want to claim that spot. If they indicate they want to claim a seat, prompt them for their name and insert it into the array to show that they've been seated, like so:

# Row 1 seat 1 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 1 seat 3 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 1 seat 4 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 2 seat 2 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 3 seat 3 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 3 seat 4 is free. Do you want to sit there? (y/n) # user says 'y'
# What is your name? # user says "Tama"

# [
#   [None, "Pumpkin", None, None],
#   ["Socks", None, "Mimi", None],
#   ["Gismo", "Shadow", None, "Tama"],
#   ["Smokey","Toast","Pacha","Mau"]
# ]

seat_list = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

print("Row 1 seat 1 is free. Do you want to sit there? (y/n)")
response= input()
if response == "y":
    print("What is your name?")
    name = input()
    seat_list[0][0] = name
    print(seat_list)

print("Row 1 seat 3 is free. Do you want to sit there? (y/n)")
response= input()
if response == "y":
    print("What is your name?")
    name = input()
    seat_list[0][2] = name
    print(seat_list)

print("Row 1 seat 4 is free. Do you want to sit there? (y/n)")
response= input()
if response == "y":
    print("What is your name?")
    name = input()
    seat_list[0][3] = name
    print(seat_list)

print("Row 2 seat 2 is free. Do you want to sit there? (y/n)")
response= input()
if response == "y":
    print("What is your name?")
    name = input()
    seat_list[1][1] = name
    print(seat_list)

print("Row 3 seat 3 is free. Do you want to sit there? (y/n)")
response= input()
if response == "y":
    print("What is your name?")
    name = input()
    seat_list[2][2] = name
    print(seat_list)

print("Row 3 seat 4 is free. Do you want to sit there? (y/n)")
response= input()
if response == "y":
    print("What is your name?")
    name = input()
    seat_list[2][3] = name
    print(seat_list)