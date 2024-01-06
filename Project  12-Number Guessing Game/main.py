import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy": remAttempts = 10
else: remAttempts = 5

while remAttempts > 0:
    print("You have", remAttempts, "remaining to guess the number.")
    guess = int(input("Make a guess: ",))
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {number}.")
        quit()
    remAttempts -= 1
    print("Guess again")
print("You've run out of guesses, you lose.")
print(f"The answer was {number}.")


