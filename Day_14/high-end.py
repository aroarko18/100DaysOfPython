import art
from game_data import data
import random
import os


# display art
print(art.logo)


def format_data(account):
    """Takes data of the account and return it for printing"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"


should_continue = True
account_b = random.choice(data)
score = 0

while should_continue:
    # account
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    # art --- vs
    print(art.vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more follower? ").lower()
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    is_correct = check_answer(guess, follower_count_a, follower_count_b)
    # print(is_correct)
    os.system('cls')
    print(art.logo)

    if is_correct:
        score = score + 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        should_continue = False
