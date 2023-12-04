# Logan White, 11/30/2023                                                      |
# 11/30/2023-3_card_monte.py
# Classwork assignment 3 card monte
# CC BY-NC-SA 4.0
# Imports
import random


# Variables
ball = 0
cups = [1, 2, 3]
sequences = ["A", "B", "C"]


# Functions
def game_start(bal):  # Initializes the game
    print("Greetings, and Welcome to 3 Card Monte.\n"
          "in This Game You can Choose to")
    user = input("Are you the House or the Bettor? \n")
    if "bet" in user.lower():  # Chooses Better
        print("Welcome Bettor")
        bettor(bal)
    elif "hou" in user.lower():  # Chooses House
        print("The Cups Are In Your Hands")
        house()
    else:
        print("Please Choose To Play As Either the House or The Bettor")  # Repeats until Proper choice is chosen
        game_start(bal)


def sequence_a(pos):  # Sequence A, swaps the first and second cups
    print("Cups 1 & 2 Swapped")
    if pos == 1:
        pos = 2
    elif pos == 2:
        pos = 1
    else:
        pass
    return pos


def sequence_b(pos):  # Sequence B, swaps the third and second cups
    print("Cups 2 & 3 Swapped")
    if pos == 2:
        pos = 3
    elif pos == 3:
        pos = 2
    else:
        pass
    return pos


def sequence_c(pos):  # Sequence C, swaps the first and third cups
    print("Cups 1 & 3 Swapped")
    if pos == 1:
        pos = 3
    elif pos == 3:
        pos = 1
    else:
        pass
    return pos


def bettor(balance):  # If the user chooses to play against the house
    betting_question = input("Are you willing to put your money where your mouth is? Y/N\n")
    # Asks if the user wants to bet
    if "y" in betting_question.lower():  # Yes Betting
        if balance == 0:
            balance = int(input("How much money have you brought? \n $"))
        elif balance < 0 < balance:
            print(f"Your Current Balance is ${balance}")
        bet = int(input("Now, How much are you willing to bet?      \n$"))
        betting(bet, balance)  # betting version
    else:  # No Betting
        print("I'll take that as a no")
        play()  # Non betting version


def ai_cup():  # Automatically Generates A sequence of Cups then runs to make the ball hidden
    pos = random.choice(cups)
    move_amount = int(input("How many times is the cup moved? "))
    move_sequence = []
    while move_amount > 0:
        move_sequence.append(random.choice(sequences))
        move_amount -= 1

    for m in move_sequence:  # Moves The Ball
        if m == "A":
            pos = sequence_a(pos)
        elif m == "B":
            pos = sequence_b(pos)
        elif m == "C":
            pos = sequence_c(pos)
    return pos


def play():  # Non Betting Gameplay
    answer = ai_cup()  # Automatic Cup movement
    guess = input("Which cup do you believe the orb is beneath? Cup 1, Cup 2, or Cup 3 \n")
    # Checks Answer
    if "1" in guess.lower():
        print("You've Guessed Cup 1")
        if answer == 1:
            play_win(answer)  # If player Wins
        else:
            play_lose(answer)  # If player Loses
    elif "2" in guess.lower():
        print("You've Guessed Cup 1")
        if answer == 2:
            play_win(answer)
        else:
            play_lose(answer)
    elif "3" in guess.lower():
        print("You've Guessed Cup 1")
        if answer == 3:
            play_win(answer)
        else:
            play_lose(answer)
    else:
        print("Please choose a valid cup")
        play()
    play_again(0)  # asks to repeat game


def play_win(pos):
    print(f"The ball was under Cup {pos}. You Win")  # Win message


def play_lose(pos):
    print(f"The ball was under Cup {pos}. You lose")  # Lose message


def betting(bet, bal):  # Betting Gameplay
    guess = input("Which cup do you believe the orb is beneath? Cup 1, Cup 2, or Cup 3 \n")
    answer = ai_cup()  # Automatic Cup movement
    # Checks Answer
    if 1 in guess.lower():
        print("You've Guessed Cup 1")
        if answer == 1:
           bal =  bet_win(bet, answer, bal)  # If player Wins
        else:
           bal =  bet_lose(bet, answer, bal)  # if player loses
    elif 2 in guess.lower():
        print("You've Guessed Cup 1")
        if answer == 2:
           bal =  bet_win(bet, answer, bal)
        else:
           bal =  bet_lose(bet, answer, bal)
    elif 3 in guess.lower():
        print("You've Guessed Cup 1")
        if answer == 3:
            bal = bet_win(bet, answer, bal)
        else:
             bal = bet_lose(bet, answer, bal)
    else:
        print("Please choose a valid cup")
        bal = betting(bet, bal)
    play_again(bal)  # asks to repeat game


def bet_win(bet, pos, bal):
    print(f"The ball was under Cup {pos}. You won ${bet}, your balance is {bal+bet}")  # Win message
    return(bal+bet)


def bet_lose(bet, pos, bal):
    print(f"The ball was under Cup {pos}. You lost ${bet}, your balance is {bal-bet}")  # Lose message
    return(bal-bet)


def house():  # Player is the house
    # ball location and movement variables
    cup = input("Place the ball under a cup, you can place it under Cup 1, Cup 2, or Cup 3")
    move_amount = input("How many times are you moving the cup?")
    move_sequence = []
    pos = 0
    # ball placement
    if 1 in cup.lower():
        pos = 1
        print("The Ball Starts in cup 1")
    elif 2 in cup.lower():
        pos = 2
        print("The Ball Starts in cup 1")
    elif 3 in cup.lower():
        pos = 3
        print("The Ball Starts in cup 1")
    else:
        print("Please choose a valid cup")
        house()
    # Ball movement
    for i in range(move_amount):
        temp_move = (input("For move #" + (i + 1) + "which sequence do you want to use?\n"
                                                    "Sequence A: swap cup1 and cup2\n"
                                                    "Sequence B: swap cup2 and cup3\n "
                                                    "Sequence C: swap cup1 and cup3\n"
                                                    "Please Designate Sequence as A, B, or C"))
        if "A" in temp_move.upper():
            move_sequence.append("A")
        elif "B" in temp_move.upper():
            move_sequence.append("B")
        elif "C" in temp_move.upper():
            move_sequence.append("C")
        # print(move_sequence)
    # Actual movement of ball
    for m in move_sequence:
        if m == "A":
            pos = sequence_a(pos)
        elif m == "B":
            pos = sequence_b(pos)
        elif m == "C":
            pos = sequence_c(pos)
    ai_player(move_sequence[-1], pos)  # calls in AI guessing


def ai_player(cup_sequence_final, pos):
    random.seed(random.randint(0, 1000000000))
    if cup_sequence_final == "A":
        ai_guess = random.randint(1, 2)
        print(f"The AI has guessed Cup {ai_guess} the ball was under {pos}")
    elif cup_sequence_final == "B":
        ai_guess = random.randint(2, 3)
        print(f"The AI has guessed Cup {ai_guess} the ball was under {pos}")
    elif cup_sequence_final == "C":
        seq_c = [1, 3]
        ai_guess = random.choice(seq_c)
        print(f"The AI has guessed Cup {ai_guess} the ball was under Cup {pos}")
    play_again(0)


def play_again(balance):  # Asks player if they want to continue
    repeat = input("Would you like to play again? Y/N")
    if "Y" in repeat.upper():
        print("Excellent!")
        game_start(balance)
    if "N" in repeat.upper():
        print("Thank you for playing!")


# Code
game_start(0)
