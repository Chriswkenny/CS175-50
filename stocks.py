#CS 175
#Christopher Kenny

#Joe's Stock Portfolio
num_shares = 2000
purchase_price = 40.00
commission_rate = 0.03
selling_price = 42.75

#Declaring Variables
amount_paid_for_stock = 0
purchase_commission = 0
total_paid = 0
stock_sold_for = 0
selling_comission = 0
total_recieved = 0
profit_or_loss = 0

#Calculations
amount_paid_for_stock = num_shares * purchase_price
purchase_commission = amount_paid_for_stock * commission_rate
total_paid = amount_paid_for_stock + purchase_commission
stock_sold_for = num_shares * selling_price
selling_comission = commission_rate * stock_sold_for
total_recieved = stock_sold_for - selling_comission
profit_or_loss = total_recieved - total_paid

#Displays to User
print(f"Amount paid for stocks: ${amount_paid_for_stock:.2f}")
print(f"Commission paid of the purchase: ${purchase_commission:.2f}")
print(f"Anount the stock sold for: ${stock_sold_for:.2f}")
print(f"Commision paid on the sale: ${selling_comission:.2f}")
print(f"Profit (or loss): ${profit_or_loss:.2f}")
