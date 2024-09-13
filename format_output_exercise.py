#Declaring Variables
Value_1 = 0
Value_2 = 0
sum = 0
difference = 0
product = 0
integer = 0
average = 0
remainder = 0
exponent = 0

#Variable Names
var1 = "Sum:"
var2 = "Difference:"
var3 = "Product:"
var4 = "Integer Division:"
var5 = "Average:"
var6 = "Remainder:"
var7 = "Exponent:"

#User Inputs
Value_1 = int(input("Enter the first number: "))
Value_2 = int(input("Enter the second number: "))

#Calculations
sum = int(Value_1 + Value_2)
difference = int(Value_1 - Value_2)
product = int(Value_1 * Value_2)
integer = int(Value_1 / Value_2)
average = float((Value_1 + Value_2) / 2)
remainder = int(Value_1 % Value_2)
exponent = int(Value_1 ** Value_2)

#Outputs to User
print()
print(f"{var1:<20} {sum:>10}")
print(f"{var2:<20} {difference:>10}")
print(f"{var3:<20} {product:>10}")
print(f"{var4:<20} {integer:>10}")
print(f"{var5:<20} {average:>10.2f}")
print(f"{var6:<20} {remainder:>10}")
print(f"{var7:<20} {exponent:>10}")
