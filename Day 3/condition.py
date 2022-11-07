height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    # less than 12
    if age < 12:
        print("Please pay $5 for the ticket.")
    elif age <= 18:
        print("Please pay $7 for the ticket.")
    else:
        print("Please pay $12 for the ticket. ")
else:
    print("Sorry, you have to grow taller before you can ride.")