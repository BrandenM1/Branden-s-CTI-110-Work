# Branden McLean
# 10-22-2026
# Use Nested loop to validate user inputs

# Create empty list 
valid_grades = []

# Get number of scores from user as int 
num_of_scores = int(input("How many grades will you enter?: "))

#Make a for loop that runs num_of_scores times
for scores in range(1,num_of_scores + 1):
    input_score = float(input(f"Enter score #: {scores}:"))
    
    # While loop that traps the user while input_score is invalid
    while input_score < 0 or input_score > 100:
        print("Invalid grade entered!")
        print("score should be between 0-100")
        # Ask them for a new value for the input_score
        input_score = float(input(f"Enter score #: {scores} again:"))

    # Add input score to the valid_grades list
    valid_grades.append(input_score)

#All loops have broken
print(valid_grades)
        