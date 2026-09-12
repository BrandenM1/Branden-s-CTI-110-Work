# Branden McLean
# Septmeber 8th, 2026
# Simulate banking

# Get name of user
Custo_name = input("Enter your name: ")

# Display Welcome message
print(Custo_name,"Welcome, Bank of Earth")

#Get initial Balance from User 
balance = 1000.00

print("current balance of:", balance)

# Get amount to withdraw

withdraw_amount = float(input("Amount to withdraw: "))

# Do Calculations
new_balance = balance-withdraw_amount

# Display balance 
print("current balance of: " , new_balance)