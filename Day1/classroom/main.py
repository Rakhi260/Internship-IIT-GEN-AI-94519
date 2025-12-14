import random

number = random.randint(1, 20)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1–20: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print("Correct! The number was", number)
