# Condition testing
def wholeplay():
    while True: 
        try: 
            int(input("Guess a number and enter: "))
            if x == guess:
                print("Congratulations you got it!")
                # Once guessed, loop will break
                break
            elif x > guess:
                print("Your number is greater than the correct answer.")
            elif x < guess:
                print("Your number is less than the correct answer.")