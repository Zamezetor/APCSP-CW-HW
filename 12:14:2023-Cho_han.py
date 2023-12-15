# Logan White 12/14/2023
# 12:14:2023-Cho_han.py
# Cho_han Game
# CC BY-NC-SA 4.0
# Imports
import random


# Variables


# Functions
def dice_display(bet, even_odd, yen):  # rolls and displays the roll of a dice
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
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
    if dice_2 == 1:
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
    dice_calc(dice_1, dice_2, bet, even_odd, yen)


def yen_check(yen):  # Does the Player have too much or not enough money
    while 1000 > yen or yen > 5000:
        if yen < 1000:
            print("You Need At Least ￥1000 To Play Here.")
        elif yen > 5000:
            print("The Dealer Cannot Bet More Than ￥5000.")
        yen = int(input("How Much Money Do You Have?  ￥"))
    return yen


def betting(yen):  # Betting function
    bet = int(input(f"You Have ￥{yen}, How Much Will You Bet?  ￥"))
    while not (bet >= 0 or bet <= yen):
        if bet >= 0:
            print("You Cannot Bet Less Than ￥0")
        if bet <= yen:
            print(f"You Cannot Bet More Than ￥{yen}")
    return bet


def bet_on_even_odd():  # Asks if you will bet on even or odd
    e_o_ask = input("Choose: Even Or Odd:  ")
    if "O" in e_o_ask.upper():
        return "Odd"
    elif "E" in e_o_ask.upper():
        return "Even"


def play_again(yen):  # Asks player if they want to continue
    if yen > 1000:  # Makes sure the player has enough money
        repeat = input("Would You Like To play Again? Y/N\t")
        if "Y" in repeat.upper():
            print("Excellent!")
            game_start(yen)
        else:
            print("Thank You For Playing!")
    else:
        print("Sorry but you do not have enough money to play again")


def dice_calc(dice_1, dice_2, bet, even_odd, yen):  # Roll Even or Odd
    dice_total = dice_1 + dice_2
    print(f"{dice_total} is the total roll")
    if dice_total % 2 == 1 and even_odd == "Odd":
        win(bet, yen)
    elif dice_total % 2 == 0 and even_odd == "Even":
        win(bet, yen)
    else:
        lose(bet, yen)


def win(bet, yen):  # If Win
    balance = (yen - bet) + (bet * 2 - (bet * 0.1))
    print(f"You win ￥{(bet * 2 - (bet * 0.1))}, Your Total is ￥{balance}")
    play_again(balance)


def lose(bet, yen):  #If Lose
    balance = (yen - bet)
    print(f"You Lost ￥{bet}, Your Total is ￥{balance}")
    play_again(balance)


def game_start(yen):  # Initializes the game
    yen = yen_check(yen)
    bet = betting(yen)
    even_odd = bet_on_even_odd()
    dice_display(bet, even_odd, yen)


# Code
game_start(0)
