import random

def wholeplay():
    while True: 
        try: 
            x= random.sample(range(0,100))
            guess= int(input("Guess a number and enter: "))
        except ValueError:
            print("Invalid input. Please do enter a number to try again.")
            continue
        else:
            break
    return x, guess
    
# Condition testing
    if x == guess:
        print("Congratulations you got it!")
    # Once guessed, loop will break
        break
    elif x > guess:
        print("Your number is greater than the correct answer.")
    elif x < guess:
        print("Your number is less than the correct answer.")