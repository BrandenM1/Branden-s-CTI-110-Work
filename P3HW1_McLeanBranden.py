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

avg = total/ len(Module)

print(f'{"avg:":<20} {avg:.2f}')

print("------------------------------------------------------")
#Round average to the nearest integer
avg = round(avg)

# Branching to determine letter grade based on the average 
if avg >= 90:
    grade_report = "A"
elif avg >=80:
    grade_report = "B"
elif avg >=70:
    grade_report = "C"
elif avg >=60: 
    grade_report = "D"
else:
    grade_reort = "F"
    
print()
print(f"Your average is {avg}, so your letter grade is {grade_report}")