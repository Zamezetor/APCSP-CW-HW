# Logan White 12/15/2023
# 12/15/2023-Collatz.py
# Collatz Number sequence
# CC BY-NC-SA 4.0
# Imports
import sys
# Variables
sys.setrecursionlimit(20000)
original = int(input("Please Input A Number To Collatz Sequence:  "))
length_dictionary = {'1':"Short Sequence"}
# Functions
def even_num(num):
    num = int(num / 2)
    return num


def odd_num(num):
    num = int((3 * num) + 1)
    return num


def sequence_check(original):
    collatz_list = []
    num = original
    while num != 1:
        collatz_list.append(num)
        if num % 2 == 1:
            num = odd_num(num)
        elif num % 2 == 0:
            num = even_num(num)
    if num == 1:
        print("The Collatz Sequence is complete.")
        collatz_list.append(num)
        print(collatz_list)
        is_long(original,collatz_list)
        print(f"{str(original)} is a {length_dictionary[(str(original))]}")

    else:
        print("We done screwed up")


def is_long(original,collatz_list):
    if len(collatz_list) > original:
        length_dictionary.update({str(original):"Long Sequence"})
    else:
        length_dictionary.update({str(original):"Short Sequence"})

        
def proportion(original):
    long_seq = 0
    short_seq = 0
    for i in range(original-1,0,-1):
        sequence_check(i)
    for i in range(original,0,-1):
        if length_dictionary[(str(i))] == "Long Sequence":
            long_seq += 1
        elif length_dictionary[(str(i))] == "Short Sequence":
            short_seq += 1
    print(length_dictionary)
    print(short_seq)
    print(long_seq)
            
        

        
# Code
sequence_check(original)
proportion(original)
