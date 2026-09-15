# Branden McLean
# Septmeber 15th, 2026
# Calculate componets of a circle using pi from the math library

import math 


# Get radius from user 
radius = float(input("Enter radius of circle: "))

print()

#Calculate diameter
diameter = 2 * radius

#Display diameter using an f-string
print(f"The diameter of the circle is {diameter:.1f} ")

#Calculate circumfrence 
circumfrence = 2* math.pi * radius

# Display circumfrence using f-string
print(f"The circumfrence is {circumfrence:.2f}")

# Calculate the area
area = math.pi * math.pow (radius, 2)

#Diplay area with f-string
print(f"The area of the cricle is {area:.3f}")