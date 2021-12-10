#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

import random

def askNums():
    while True:
        try:
            firstnum= int(input("Enter your first number; any number ranging from 0-9: "))
            if firstnum not in range(0,9):
                print("Invalid input. Number is out of range.")
                continue
            secondnum= int(input("Enter your second number; any number ranging from 0-9: "))
            if secondnum not in range(0,9):
                print("Invalid input. Number is out of range.")
                continue
            thirdnum= int(input("Enter your third number; any number ranging from 0-9: "))