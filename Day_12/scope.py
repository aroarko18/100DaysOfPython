# Local
def localFunction():
    capital = "Dhaka"
    print(capital)
localFunction()
# print(capital) ---- It can't be accessible because of local variable

# Global
capital_city = "Kuala Lumpur"
def globalFunction():
    print(capital_city)
globalFunction()
print((capital_city))
