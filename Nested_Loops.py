# Use a nested loop to stimulate a clock

# Loop to run 12 times for the hours
for Hour in range(1,13):
    #print(Hour)
    
    # Inner Loop that runs 60 times for the minutes 
    for Minute in range(0,60):
        if Minute <=9:
            print(f"{Hour}:0{Minute}")
        else:    
            print(f"{Hour}:{Minute}")
