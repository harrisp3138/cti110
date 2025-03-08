#
#
# Patrick Harris
# 3/4/2025
# P3LAB
# if/else, floor division, displaying coin combinations
# 
# Get money amount from user as float
# Convert money into an int (* 100, = total cent value)
# Store the amount (in cents) as a variable
# 
# 
# 
# 
# 



# dollar = 1.00
# quarter = 0.25
# dime = 0.10
# nickel = 0.05
# penny = 0.01

print("This program calculates the most efficient demination distrubition for a given amount of money.")
print("--" * 20)
amount = float(input('Enter an amount of money as a float: $'))
if amount == 0.00 or 0:
    print("$0.00 entered.")

amount = int(amount * 100) #converts float to int for easier calculations


num_dollars = amount // 100 #floor division to find number of dollars without remainder
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} dollar")
    else:
        print(f"{num_dollars} dollars")
amount = amount - (num_dollars * 100) 


num_quarters = amount // 25
if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} quarter")
    else:
        print(f"{num_quarters} quarters")
amount = amount - (num_quarters * 25)


num_dimes = amount // 10
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} dime")
    else:
        print(f"{num_dimes} dimes")
amount = amount - (num_dimes * 10)


num_nickels = amount // 5
if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} nickel")
    else:
        print(f"{num_nickels} nickels")
amount = amount - (num_nickels * 5)


num_pennies = amount // 1
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} penny")
    else:
        print(f"{num_pennies} pennies")
amount = amount - (num_pennies * 1)


input("Press Enter to exit.")