import random

count = 1
num = random.randint(1,100)
while True:
    guess = int(input("Guess the number: "))
    if guess == num:
        print("You guessed it!")
        break
    elif guess > num:
        print("Too high!")
        count += 1
    elif guess < num:
        print("Too low!")
        count += 1
    else:
        print("Invalid input pls choose between 1 and 100")

print("You guessed the number in", count, "tries")