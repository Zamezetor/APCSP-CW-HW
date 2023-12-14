# Logan White 12/14/2023
# 12:14:2023-Cho_han.py
# Cho_han Game
# CC BY-NC-SA 4.0
# Imports
import random


# Variables
yen = 0


# Functions
def dice_display():  #rolls and displays the roll of a dice
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    if dice_1 == 1:
        print("  _____\n  |   |\n  | o |\n  |   |\n  _____")
        print(f"Dice one rolls a {dice_1}")
    elif dice_1 == 2:
        print("  _____\n  |o  |\n  |   |\n  |  o|\n  _____")
        print(f"Dice one rolls a {dice_1}")
    elif dice_1 == 3:
        print("  _____\n  |o  |\n  | o |\n  |  o|\n  _____")
        print(f"Dice one rolls a {dice_1}")
    elif dice_1 == 4:
        print("  _____\n  |o o|\n  |   |\n  |o o|\n  _____")
        print(f"Dice one rolls a {dice_1}")
    elif dice_1 == 5:
        print("  _____\n  |o o|\n  | o |\n  |o o|\n  _____")
        print(f"Dice one rolls a {dice_1}")
    elif dice_1 == 6:
        print("  _____\n  |o o|\n  |o o|\n  |o o|\n  _____")
        print(f"Dice one rolls a {dice_1}")
    elif dice_2 == 1:
        print("  _____\n  |   |\n  | o |\n  |   |\n  _____")
        print(f"Dice one rolls a {dice_2}")
    elif dice_2 == 2:
        print("  _____\n  |o  |\n  |   |\n  |  o|\n  _____")
        print(f"Dice one rolls a {dice_2}")
    elif dice_2 == 3:
        print("  _____\n  |o  |\n  | o |\n  |  o|\n  _____")
        print(f"Dice one rolls a {dice_2}")
    elif dice_2 == 4:
        print("  _____\n  |o o|\n  |   |\n  |o o|\n  _____")
        print(f"Dice one rolls a {dice_2}")
    elif dice_2 == 5:
        print("  _____\n  |o o|\n  | o |\n  |o o|\n  _____")
        print(f"Dice one rolls a {dice_2}")
    elif dice_2 == 6:
        print("  _____\n  |o o|\n  |o o|\n  |o o|\n  _____")
        print(f"Dice one rolls a {dice_2}")
    dice_calc(dice_1,dice_2)

def yen_check(yen):
    while 1000 > yen or yen > 5000:
        if yen < 1000:
            print("You Need At Least ￥1000 To Play Here.")
        elif yen > 5000:
            print("The Dealer Cannot Bet More Than ￥5000.")
        yen = int(input("How Much Money Do You Have?  ￥"))
    return yen

def betting(yen):
    bet = input(f"You Have ￥{yen}, How Much Will You Bet?  ￥")
    while not(bet >= 0 or bet <= yen):
        if bet >= 0:
            print("You Cannot Bet Less Than ￥0")
        if bet <= yen:
            print(f"You Cannot Bet More Than ￥{yen}")
    return bet

def bet_on_even_odd(even_odd):
    e_o_ask = input("Choose: Even Or Odd:  ")
    if "O" in e_o_ask.upper():
        return "Odd"
    elif "E" in e_o_ask.upper():
        return "Even"

def play_again(yen):  # Asks player if they want to continue
    if yen > 1000:  # Makes sure the player has enough money
        repeat = input("Would You Like To play Again? Y/N")
        if "Y" in repeat.upper():
            print("Excellent!")
            game_start(yen)
        if "N" in repeat.upper():
            print("Thank You For Playing!")

def dice_calc(dice_1,dice_2):
    
def game_start(yen):
    yen = yen_check(yen)
    bet = betting(yen)
    even_odd = bet_on_even_odd()
    dice_display()


# 一二三四五六
# Code
game_start(yen)

