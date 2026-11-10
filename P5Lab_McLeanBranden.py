# Using Functions and module import to complete assigments 
# Self-Check out program

import random 

def disperse_change(change):
    
    if change == 0: 
        print("No change due")
    #Calculate the amount of each coin needed 
    
    num_dollars = change // 100
    change - change - (num_dollars * 100)
    num_quarters = change // 25 
    change = change - (num_quarters * 25)
    num_dimes = change // 10
    change = change - (num_dimes * 10) 
    num_nickles = change // 5
    change = change - (num_nickles * 5)
    num_pennies = change // 1
    change = change -(num_pennies * 1)
    
    #Display coins owed 
    if num_dollars > 0:
        print(num_dollars,)
        if num_dollars == 1: 
            print("Dollar")
        else:
            print(" Dollars")
    
    if num_quarters > 0:
        print(num_quarters,)
        if num_quarters == 1: 
            print("Quarter")
        else:
            print(" Quarters")

    if num_dimes > 0:
        print(num_dimes,)
        if num_dimes == 1: 
            print("Dime")
        else:
            print(" Dimes")
                
    if num_nickles > 0:
        print(num_nickles,)
        if num_dollars == 1: 
            print("Nickle")
        else:
            print(" Nickles")

    if num_pennies > 0:
        print(num_pennies,)
        if num_pennies == 1: 
            print("Penny")
        else:
            print(" Pennys")

def main():
    
    #Generate a random flow with 2 decimal places as the amount that the customer owe

    amount_owed = round(random.uniform(0.01, 100.00), 2)
    
    #display the amount owed 
    print(f"You owe ${amount_owed:.2f}")
    #Prompt the uer to enter a float as the cash they will put into the checkout machine. 
    amount = float(input("Enter the amount of money as a float:"))
    
    #calculate change owed 
    change = amount - amount_owed 
    
    #Display change owed 
    print(f"Change is: ${change:.2f}")
    
    #Convert change owed to an integer 
    change = round(change * 100)
    
    #Call the function and pass the change_owed as the parameter 
    disperse_change(change)
main()   