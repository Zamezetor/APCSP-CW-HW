# Logan White, 12/13/2023                                                      |
# 12:13:2023-Mastermind.py
# Mastermind Game 
# CC BY-NC-SA 4.0
# Imports
import random
# Variables
number = [10,10,10,10]
guess = ""
guess_list = ""
# Functions
def seq_gen():  # Generates a sequence of random numbers
    while len(number) < 4:
        generated_num = random_generator
        for i in number:
            while number[i] == generated_num:
                generated_num = random_generator
                print(generated_num)
            if number[i] != generated_num:
                number.append(generated_num)
                print(number)
            
def random_generator():
    return random.randint(0,9)
# Code
