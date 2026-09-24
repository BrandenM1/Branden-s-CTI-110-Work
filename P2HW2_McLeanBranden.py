# Branden McLean
# Spetember 22nd, 2026
# PSHW2 
# This is programmed to give module scores 


# Enter Module Scores
Mod1= float(input(" Enter Mod1 Score: "))
Mod1= float(input(" Enter Mod1 Score: "))
Mod2= float(input(" Enter Mod2 Score: "))
Mod3= float(input(" Enter Mod3 Score: "))
Mod4= float(input(" Enter Mod4 Score: "))
Mod5= float(input(" Enter Mod5 Score: "))
Mod6= float(input(" Enter Mod6 Score: "))

# Mod scores
Module = [Mod1,Mod2,Mod3,Mod4,Mod5,Mod6]

# Display High/Lowest Grade
print("-------------Results--------------")

print(f"The Lowest Score entered is: {min(Module):.2f}")

print(f"The Highest Score entered is: {max(Module):.2f}")

print(f"All scores added up are: {sum(Module):.2f}")

total=sum(Module)

print(f"Your average for all Modules: {total/6:.2f}")