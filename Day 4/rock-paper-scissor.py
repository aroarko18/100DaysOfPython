import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_decision == 0:
    print(rock)
elif user_decision == 1:
    print(paper)
elif user_decision == 2:
    print(scissors)
else:
    print("Please enter a valid number.")

random_pc_count = random.randint(0, 2)
if random_pc_count == 0:
    print(rock)
elif random_pc_count == 1:
    print(paper)
elif random_pc_count == 2:
    print(scissors)


if user_decision == 0 and random_pc_count == 1:
    print("You lose..")
elif user_decision == 0 and random_pc_count == 2:
    print("Congratulations! You win...")
elif user_decision == 1 and random_pc_count == 0:
    print("Congratulations! You win...")
elif user_decision == 1 and random_pc_count == 2:
    print("You lose..")
elif user_decision == 2 and random_pc_count == 0:
    print("You lose..")
elif user_decision == 2 and random_pc_count == 1:
    print("Congratulations! You win...")
elif user_decision == random_pc_count:
    print("Ooops! It's draw..")