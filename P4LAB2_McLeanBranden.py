# Branden McLean
# 10/20/2026
#Nested loops 
# Create the Variable that controls the while loop
# This value is temporary
Run_Again = "yes"
while Run_Again == "yes": 
    
    #Get an integer from the user 
    integer = int(input("Enter a number: "))
    
    #Check if integer is positive \
    if integer >= 0: 
        # Display Multiplication 
        for num in range(1,13):
            print(f"{integer}*{num}={integer * num}")
        
    # If the number is negative
    else:
        print("Error, no negative numbers allowed")        
    
    
    
    
    
    
    # Allow the user to give a new value to run again
    Run_Again = input("Run the program again? ").lower()


# Loop breaks here 
print("Program ended, goodbye!")

