# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.
import random

# program asks user to input a number along with input validation
def play():
    while True:
        try:
            guess= int(input("Enter your guess: "))
            if guess not in range(0,100):
                print("Invalid input. Number is out of range.")
                continue
        except ValueError:
            print("Invalid input. Please do enter a number.")
            continue
        else:
            break
    return guess

def checkNumber(userguess, correctguess):
    if userguess > correctguess:
        print("Greater than")
    elif userguess < correctguess:
        print("Less than")
    elif userguess == correctguess:
        print("Congratulations! You guessed the number!")

def game(winningNum):
    guessNum = ("")
    while guessNum != winningNum:
        guessNum = play()
        checkNumber(guessNum, winningNum)
        continue

def guess():
    correctNum= random.randint(0,100)
    game(correctNum)
    return correctNum

def onceMore():
     while True:
        yn = input("Do you wish to try again?: ")
        yn = yn.lower()
        if yn == 'y':
            print("\n")
            play()
            guess()
        elif yn == 'n':
            print("Thanks for playing!")
            break
        else:
            print("\n")
            print("Please enter y if you want to play again, or enter n to exit the game.")
        break

userguess= play()
correctguess= guess()
onceMore()