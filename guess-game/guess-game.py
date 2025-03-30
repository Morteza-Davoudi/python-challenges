import random
randNum = random.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == randNum:
        print("You guessed right!")
        break
    elif guess > randNum:
        print("Too high!")
    elif guess < randNum:
        print("Too low!")