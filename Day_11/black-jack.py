logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
print(logo)

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# user_card
user_card = []

import random
user_card_1 = random.choice(card)
user_card_2 = random.choice(card)

user_card_score = user_card_1 + user_card_2

if user_card_score >= 22:
    user_card_2 = 1
user_card.append(user_card_1)
user_card.append(user_card_2)
user_card_score = user_card_1 + user_card_2



# computer_card
pc_card = []
pc_card_1 = random.choice(card)
pc_card_2 = random.choice(card)

pc_card_score = pc_card_1 + pc_card_2

if pc_card_score >= 22:
    pc_card_2 = 1

pc_card.append(pc_card_1)
pc_card.append(pc_card_2)
pc_card_score = pc_card_1 + pc_card_2

print(f"Your cards: {user_card}, current score: {user_card_score}")
print(f"Computer's first card: {pc_card_1}")

if user_card_score == 21 and pc_card_score != 21:
    print("User won!")
elif user_card_score != 21 and pc_card_score == 21:
    print("Computer Won!")

while pc_card_score < 17:
    pc_card_more = random.choice(card)
    card.append(pc_card_more)
    pc_card_score = pc_card_score + pc_card_more
    
while user_card_score < 17:
    if input("Type 'y' to get anotheer card, type 'n' to pass: ") == "y":
        user_card_more = random.choice(card)
        user_card.append(user_card_more)
        user_card_score = user_card_score + user_card_more
        print(f"Your cards {user_card}, current score {user_card_score}")
    

if user_card_score > pc_card_score:
    print(f"Your final hand : {user_card}, final score: {user_card_score}")
    print(f"Computer's final hand: {pc_card}, final score: {pc_card_score}")
    print("You win")
elif user_card_score == pc_card_score:
    print(f"Your final hand : {user_card}, final score: {user_card_score}")
    print(f"Computer's final hand: {pc_card}, final score: {pc_card_score}")
    print("It's draw")
else:
    print(f"Your final hand : {user_card}, final score: {user_card_score}")
    print(f"Computer's final hand: {pc_card}, final score: {pc_card_score}")
    print("You lose")