import art
from game_data import data
import random
print(art.logo)

def get_random_account():

    return random.choice(data)

get_random_account()