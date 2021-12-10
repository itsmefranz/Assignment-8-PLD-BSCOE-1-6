#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

import random

# 'checker', compares userNums and winningNums to see if they have won or lost
def checker(userNums, winningNums):

    if userNums == winningNums:
        print ("\nCongratulations! You Win!\n")
        print ("Your numbers: ", userNums)
        print ("The winning lottery numbers are: ", winningNums, "\n")
    else:

        print ("\nSorry, you lose...\n")
        print ("Your numbers: ", userNums)
        print ("The winning lottery numbers are: ", winningNums, "\n")


# program asks user to input three number along with input validation
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
            if thirdnum not in range(0,9):
                print("Invalid input. Number is out of range.")
                continue
        except ValueError:
            print("Invalid input. Please do enter a number.")
            continue
        else:
            break
    numList= [firstnum, secondnum,thirdnum]
    return numList

# program generates three winning numbers that would be random
def getWinningNums():
    winnum1, winnum2, winnum3= random.sample(range(0,9),3)
    winningList= [winnum1, winnum2, winnum3]
    return winningList

#will asks if user wishes to try again
def onceMore():
     while True:
        yn = input("Do you wish to try again?: ")
        yn = yn.lower()
        if yn == 'y':
            print("\n")
            askNums()
            getWinningNums()
            checker(userNums,winningNums)
        elif yn == 'n':
            print("Thanks for playing!")
            break
        else:
            print("\n")
            print("Please enter y if you want to play again, or enter n to exit the game.")

userNums= askNums()
winningNums = getWinningNums()
checker(userNums, winningNums)
onceMore()