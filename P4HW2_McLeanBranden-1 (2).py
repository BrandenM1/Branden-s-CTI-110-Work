#Branden McLean
#10-23-2026
#Salary Calculator with loops

#Request employee info 
name = input("Enter employee's name or 'done' to finish: ")

#Create Accumulator Variables for overtime pay, regular pay, gross pay and employee count
overtimepay_total = 0
regularpay_total = 0 
grosspay_total = 0
employee_count = 0

while name.lower() != 'done':
    # Add employee count plus one
    employee_count += 1 
    #Ask for employee info
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay rate? "))


#Calculate Pay 

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate 
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0 
        regular_pay = hours * rate
        gross_pay = regular_pay



#Add accumulator totals 
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay
    name = input("Enter employee's name or 'done' to finish: ")






# Display results for this employee 

    print("------------------------------------")
    print("Employee Name:", name)
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime Pay":<15}{"Gross Pay":<12}')
    print("----------------------------------------------------------")
    print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')


print("total number of employees entered: ", employee_count)
print(f"Total amount paid for overtime: {overtimepay_total: ,.2f}")
print(f"Total amount paid for regular time: $ {regularpay_total: ,.2f}") 
print(f"Total amount paid in gross: $ {grosspay_total: ,.2f}")

# Ask user for another name 
name = input("Enter employee name or 'Done' to quit: ")

# Loop ends here
# Display total for all employees 
