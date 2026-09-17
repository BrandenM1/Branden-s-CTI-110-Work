# Branden McLean
# September 17th, 2026
# Use the dictionary to determine of fuel needed from user input

# Create the dictionary - cars are the keys and mpgs are the values
cars = {"camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Select only the keys
keys= cars.keys()

#Display the keys
print()
print(keys)

#Get a car choice from user 
Car_Choice = input("Enter a car to see MPG: ")

# Using car choice, pull the associated MPG from the dictionary 
mpg = cars[Car_Choice]
# Display Car choice and MPG 
print(f"The {cars} gets {mpg} mpg.")

# Get miles to drive from user as a float

miles = float(input(f"How many miles will you drive the {Car_Choice}?"))

#Calculate gallons of gas needed 
gallon=miles/mpg

#Display 
print (f"{gallon} gallons of gas are needed to drive the {Car_Choice} {miles} miles .")