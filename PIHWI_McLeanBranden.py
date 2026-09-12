#Branden McLean
#September 10th, 2026
# Inputs, outputs, and mathematical calculations

print("------ Calculating Exponents------")
print()
print()

# Get base value from user and convert to int
base_value = int(input("Enter a base value: "))

# Get exponent from user and convert to int
exponent = int(input("Enter Exponent"))

# Calculate
answer = base_value ** exponent

# Display answer 
print(base_value, "raised to the power of", exponent, "is", answer)
print()
print()
print()

print("------ Addition and Subtracting------")


# Get three integers from user
num1 = int(input("Enter starting number: " ))
num2 = int(input("Enter a number to add: "))
num3= int(input("enter number to subtract: "))

print()

#Display results
print(num1,"+", num2, "-", num3, "=", num1 + num2 - num3)
