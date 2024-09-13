#Store_Items Assignment
#Christopher Kenny
#CS 175

#Constant Variables
item1 = "fries"
item2 = "cheeseburger"
item3= "soda"
myName = "Chris"
taxRate = 0.1
fee = 2.99

#Declare Variables
item1_cost = 0.00
item2_cost = 0.00
item3_cost = 0.00
subTotal = 0.00
taxAmount = 0.00
grandTotal = 0.00

#Set Variables (Cost of Food items)
item1_cost = float(input(f"Enter the price of {item1}: "))
item2_cost = float(input(f"Enter the price of {item2}: "))
item3_cost = float(input(f"Enter the price of {item3}: "))
subTotal = item1_cost + item2_cost + item3_cost
taxAmount = subTotal * taxRate
grandTotal = subTotal + taxAmount + fee

#Outputs to User
print(f"The cost of {item1} is ${item1_cost:.2f}")
print(f"The cost of {item2} is ${item2_cost:.2f}")
print(f"The cost of {item3} is ${item3_cost:.2f}")
print(f"The subtotal is ${subTotal:.2f}")
print(f"The tax is ${taxAmount:.2f}")
print(f"The total is ${grandTotal:.2f}")
print(f"{myName} paid the final bill of ${grandTotal}")

