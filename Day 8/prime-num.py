#Write your code below this line ๐
def prime_checker(number):
    for value in range(2, number):
        if number % value == 0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")




#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))

prime_checker(n)