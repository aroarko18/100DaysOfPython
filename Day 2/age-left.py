# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

year_left = 90 - int(age)

days = year_left * 365
weeks = year_left * 52
months = year_left * 12

# print("You have " + str(days) + " days, " + str(weeks) + " weeks, and "+ str(months) + " months left")


print(f"You have {days} days, {weeks} weeks, and {months} months left")


