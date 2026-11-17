import random

def dice():
    attempts = 0
    while True:

        dice = int(random.randint(1,6))
        try:
            guess = int(input("Enter a number from 1 to 6: "))
            attempts+=1
            print(f"The die rolled : {dice}")
            print(f"Attempts: {attempts}")
            if(guess == dice):
                print("Congratulations you guessed right!")
                break
            else:
                print("You guessed wrong :( keep trying!)")
        except ValueError:
                print("Please only enter a number")


print("hi guys let's do some guessing")
dice()