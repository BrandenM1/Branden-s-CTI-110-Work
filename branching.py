# Use if/else statements 

# Get age 
age = int(input("Enter your age: "))

# Condition to determine if they are senior 
if age >= 65:
    print("You are a Senior Citizen!")
    discount = 0.15
else:
    print("You are not a Senior Citizen!")
    discount = 0.00
    
# This part will always run, it is outside the else
purchase = 100.00
discount_amount = purchase * discount
print(f"Your discount is ${discount_amount:.2f}")
