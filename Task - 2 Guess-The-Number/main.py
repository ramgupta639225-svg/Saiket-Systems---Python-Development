import random

number = random.randint(1, 100)
attempts = 0

print("\nWelcome to Guess the Number Game!")
print("Guess a number between 1 and 100.")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < 1 or guess > 100:
        print("Choose a number between 1 and 100.")
        continue

    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("\nCongratulations! You guessed the number.")
        print("The number was:", number)
        print("Total attempts:", attempts)
        break

        