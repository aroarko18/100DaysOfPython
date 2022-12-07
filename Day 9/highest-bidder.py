# import os


def clear():
   os.system("clear")

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}

def bid_result(all_bidders):
    highest_bid = 0
    for bidder in all_bidders:
        new_price = all_bidders[bidder]
        if new_price > highest_bid:
            highest_bid = new_price
            name = bidder
    print(f"The winner is {name} with a bid of ${highest_bid}")

still_bidder = True

while still_bidder:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    still_continue = input("Are there any other bidders? Type 'yes'  or 'no'.\n")
    if still_continue == "no":
        still_bidder = False
    # elif still_bidder == "yes":
    #     clear()

bid_result(bids)