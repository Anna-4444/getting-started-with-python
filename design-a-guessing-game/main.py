import random

random = random.randint(1, 100)
correct_guess = False

while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")
    try:
        number = int(user_input)
    except:
        print("enter a number")

    if number == random:
        correct_guess = True
    elif number > random:
        print("You guessed too high")
    elif number < random:
        print("You guessed too low")

print("You guessed the right number!")

