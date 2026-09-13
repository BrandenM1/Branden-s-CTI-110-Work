# Branden McLean
# September 11th, 2026
# P1HW2
# This calculates all travel exspenses for an upcoming trip 

# Ask user how much money is willing to be spent during trip
budget= int(input("enter budget: " ))

# Ask user where they are traveling to
location= input("enter location: ")

#Ask user for estimated cost of Fuel
fuel= int(input("enter fuel cost: "))

# Ask user estimated cost for lodging 
lodging= int(input("enter lodging cost: "))

# Ask User about food exspenses 
food= int(input("enter cost of food: "))

#Calculate the remianing balance after all exspenses 
remaining_money= budget - fuel - lodging - food 

# Display Travel Exspense information
print("----------------Travel Exspense---------------")
print("Location:", location)
print("Inital budget:", budget)

print("Fuel:", fuel)
print("Accommodation:", lodging)
print("Food:", food)

print("Remaining balance:", remaining_money)