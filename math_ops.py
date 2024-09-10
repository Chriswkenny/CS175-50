# CS 175
# Christopher Kenny
# Problem 3

#User Value Inputs
Value_1 = int(input("Enter any whole number here: "))
Value_2 = int(input("Enter another whole number here: "))

#Calculations
sum = Value_1 + Value_2
difference = Value_2 - Value_1
product = Value_1 * Value_2
average = Value_1 + Value_2 / 2
distance = abs(Value_2 - Value_1)
maximum = max([Value_1, Value_2])
minimum = min([Value_1, Value_2])

#Displays to User
print(f"The sum of your chosen values is {sum}")
print(f"The difference between your chosen values is {difference}")
print(f"The product of your chosen values is {product}")
print(f"The average of your chosen values is {average}")
print(f"The distance between your chosen numbers is {distance}")
print(f"The maximum (larger) of your two numbers is {maximum}")
print(f"The minimum (smaller) of your two numbers is {minimum}")
