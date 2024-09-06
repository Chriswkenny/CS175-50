# CS175
# Christopher Kenny
# Problem 2

#Initial Balance
initial_balance = 1000.00

#Earns 0.5 percent interest per year
interest_rate = 0.05

#Balance after first year
balance_after_first_year = initial_balance * (1 + interest_rate)

#Change in bank account over 1 year
print(f"Your balance after 1 year in savings is {balance_after_first_year}")

#Balance after second year
balance_after_second_year = balance_after_first_year * (1 + interest_rate)

#Change in bank account after 2 years
print(f"Your balance after 2 years in savings is {balance_after_second_year}")

#Balance after third year
balance_after_third_year = balance_after_second_year * (1 + interest_rate)

#Change in bank account after 3 years
print(f"Your balance after 3 years in savings is {balance_after_third_year}")
