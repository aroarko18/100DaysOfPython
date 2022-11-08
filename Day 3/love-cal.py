# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


two_name = name1 + name2
lower_name = two_name.lower()

# compare with true

true_t = lower_name.count("t")
true_r = lower_name.count("r")
true_u = lower_name.count("u")
true_e = lower_name.count("e")

true_value = true_t + true_r + true_u + true_e
# print(true_value)


# compare with love

love_l = lower_name.count("l")
love_o = lower_name.count("o")
love_v = lower_name.count("v")
love_e = lower_name.count("e")

love_value = love_l + love_o + love_v + love_e

score = str(true_value) + str(love_value)


# comments for love
if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")