#Write your code below this line 👇
import math






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height=test_h, width=test_w, cover=coverage):
    number_of_cans = (height * width) / cover
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")

paint_calc()

