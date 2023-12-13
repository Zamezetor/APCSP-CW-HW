# Logan White, 12/13/2023                                                      |
# 12:13:2023-Mastermind.py
# Mastermind Game 
# CC BY-NC-SA 4.0
# Imports
import random


# Variables


# Functions
def game_start():
    guess = input("Please input a 4 digit sequence of numbers:\t")
    guess_list = listify(guess)
    number = seq_gen()
    num_check(guess_list,number)

    
def seq_gen():  # Generates a sequence of random numbers
    digit_list = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(digit_list)
    return digit_list[:4]


def listify(guess):
    num_list = []
    for i in guess:
        num_list.append(int(i))
    return num_list


def num_check(g_list,num):
    color_code = ["Grey","Grey","Grey","Grey"]
    num = [1,2,3,7]
    print(g_list, num)
    for i in range(4):
        if g_list[i] == num[i]:
            print(color_code)
            color_code.pop(i)
            color_code.insert(i,"Green")
            print(color_code)
            


# Code
game_start()
