import random


def get_integer(prompt):
    # while True:
    temp = input(prompt)
    # return prompt.isnumeric()
    # return int(temp)


# print(input.__doc__)
# print("*" * 80)
# print(get_integer.__doc__)
help(print)

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    # guess = get_integer(": ")
    guess = input(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    if get_integer(guess) is False:
        print("Please enter a valid number!")
        continue
    if get_integer(guess) is True:
        guess = int(guess)
        if guess < answer:
            print("Please guess higher")
        elif guess > answer:  # guess must be greater than answer
            print("Please guess lower")
