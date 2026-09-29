# Use if/elif/else
# Get age 
age = int(input("Enter your age: "))


# Determine the age group
# The first conditon is always an if 

if age >= 0 and age <= 12:
    age_group = "Child"
elif age <= 19:
    age_group = "Teen"
elif age <= 64:
    age_group = "Adult"
elif age >= 65:
    age_group = "Senior"
print(f"At age {age} you are a {age_group}")        