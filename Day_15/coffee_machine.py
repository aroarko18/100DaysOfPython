MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 2. What user wants???
coffee_need = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 1. Print the report what's available
if coffee_need == "report":
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]
    print(f"Water: {water_amount}ml\nMilk: {milk_amount}ml\nCoffee: {coffee_amount}ml")
# TODO: 3. Coin calculation for payment
