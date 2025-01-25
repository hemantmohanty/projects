import random
x=int(input("Guess number"))
def Guess_Number(x):
    random_guess=random.randint(1,x)
    guess=0
    while guess != random_guess:
        guess=int(input(f"Guess a number between 1 & {x}"))
        if guess < random_guess:
            print("Sorry, too low")
        elif guess > random_guess:
            print("Sorry, too high")
    print(f"Yay, you guess currect number {random_guess}")

Guess_Number()