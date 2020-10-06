#Question 19

coins = int(input("Enter the number of cents: "))
print("Quarters: {0}".format(coins//25))
coins%=25
print("Dimes: {0}".format(coins//10))
coins%=10
print("Nickels: {0}".format(coins//5))
coins%=5
print("Pennies: {0}".format(coins))