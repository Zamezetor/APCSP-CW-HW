# Logan White 12/04/2023
# 12:04:2023-parking_spaces.py
# Classwork Assignment
# CC BY-NC-SA 4.0
# Imports
    # None
# Variables
parking_list = []
parking_list_prior = []
length_of_stay = {}


# Functions
def spot_numbers():  # asks how many spots are to be used
    space_num = int(input("How many parking spaces do you require? (0-100) "))
    # was the car there yesterday? today?
    for i in range(space_num):
        yesterday = (input(f"Was a car occupying spot {i} Yesterday? Y/N \n"))
        if "Y" in yesterday.upper():
            parking_list_prior.append("C")
        else:
             parking_list_prior.append(".")
    for i in range(space_num):
        today = (input(f"Was a car occupying spot {i} Today? Y/N \n")) 
        if "Y" in today.upper():
            parking_list.append("C")
        else:
             parking_list.append(".")
    occupancy()


def occupancy():  # How long is the car going to be there?
    for i in range(len(parking_list)):
        if parking_list[i] == "C":  # checks if there is a car in the space
            length_of_stay["Space " + str(i)] = \
                int(input(f"How many days is space {i} to be occupied? "))
        else:
            pass # if no car in space, pass


def both_days():  # Figures out which parking spots were used both days 
    spots_both_days = 0  # both days counter
    for i in range(len(parking_list)):  # was the spot used both days?
        if parking_list[i] == "C" and parking_list_prior[i] == "C":
            spots_both_days += 1
            print(f"Spot {i} was occupied both days")
        else:
            pass
    # Grammar formating
    if spots_both_days != 1:
        print(f"There were {spots_both_days} spots in use both today and "
              "yesterday ")
    elif spots_both_days == 1:
        print(f"There was {spots_both_days} spot in use both today and "
              "yesterday ")


# Code
spot_numbers()
both_days()
