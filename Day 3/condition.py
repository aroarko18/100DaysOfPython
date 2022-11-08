height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    # less than 12
    if age < 12:
        bill = 5
        print("Please pay $5 for the ticket.")
    elif age <= 18:
        bill = 7
        print("Please pay $7 for the ticket.")
    elif age >= 45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12 for the ticket. ")

    want_photo = input("Do want to have a photo? Y or N ")
    if want_photo == "Y":
        updated_bill = bill + 3
        print(f"Your total bill is ${updated_bill}")
    else:
        print(f"Thank you, your bill is only ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")