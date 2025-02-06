 # Patrick Harris
 # 2/6/2025
 # P1HW1
 # Python program using mathematical expressions 

print()
#Calculating Exponents 
print("-----Calculating Exponents-----")
print()
baseValue=int(input("Enter an integer as the base value: "))
exponentValue=int(input("Enter an integer as the exponent: "))

newValue=(baseValue ** exponentValue)
print()
print(baseValue, "raised to the power of", exponentValue, "is", str(newValue) + "!!")
print()

#Addition and Subtraction
print("-----Addition and Subtraction-----")
print()
startingInt=int(input("Enter a starting integer: "))
addInt=int(input("Enter an integer to add: "))
subtractInt=int(input("Enter an integer to subtract: "))

solution=(startingInt + addInt - subtractInt)
print()
print(startingInt, "+", addInt, "-", subtractInt, "is equal to", solution)
print()

input("Press Enter to exit")