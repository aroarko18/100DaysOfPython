# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n_year = str(year)
last_value = int(n_year[3])
second_last = int(n_year[2])

# print(last_value)
# print(second_last)

# if (((last_value and second_last) == 0) and (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)):
#     print("Leap year")
# elif(((last_value or second_last) != 0) and (year % 4 == 0)):
#     print("Leap year")
# else:
#     print("Not Leap year")

if ((year % 100 == 0) and (year % 400 == 0)):
    print("Leap year")
elif((year % 100 != 0) and (year % 4 == 0)):
    print("Leap year")
else:
    print("Not Leap year")