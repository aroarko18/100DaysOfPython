import random

logo = """
       ___                  _____ _          _  _            _             
  / __|_  _ ___ ______ |_   _| |_  ___  | \| |_  _ _ __ | |__  ___ _ _ 
 | (_ | || / -_|_-<_-<   | | | ' \/ -_) | .` | || | '  \| '_ \/ -_) '_|
  \___|\_,_\___/__/__/   |_| |_||_\___| |_|\_|\_,_|_|_|_|_.__/\___|_|  
                                                                       
"""
print(logo)

print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")

number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 5

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts == 5
print(f"You have {attempts} attempts remaining to guess the number.")

should_run = True
while should_run:
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}")
        should_run = False
    elif guess > number and attempts > 0:
        print("Too high.")
        print("Guess again")
        attempts -= 1
    elif guess < number and attempts > 0:
        print("Too low.")
        print("Guess again")
        attempts -= 1
    if attempts >= 1:
        print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
        print("You have run out of guesses, you lose.")
        should_run = False
    
    