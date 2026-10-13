import random

random = random.randint(1, 100)

while True:
    user = int(input("Guess the number:  "))
    if user < random:
        print("Lower")
    elif user > random:
        print("Higher")
    else:
        print("You Win")

        break
