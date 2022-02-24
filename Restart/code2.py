import random

c = int(input("Enter the limit of number in guess game: "))

# assigning random number to a
a = random.randint(0,c)

# printing number for learning purpose
print(a)

# start guessing number
guess = int(input("guess: "))

# if guess is equal to number
if guess == a:
    print(f"You guessed it right {guess}")

# if guess is not equal to number
else:
    while guess != a:
    # if guess is greater than random number 
        if guess < a:
            print("Guess higher")

    # if guess is lower than random number
        elif guess > a:
            print("guess lower")
        guess = int(input("guess: "))

    print("You guessed it right {}".format(guess))
