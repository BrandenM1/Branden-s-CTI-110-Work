# Branden McLean
# 10/23/2026
# P4LAB1
# Use turtle to draw a sqaure and a triangle


#Import the library
import turtle

#Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Set turtle options
pen.pensize(3)
pen.pencolor("red")
pen.shape("arrow")


# Code to draw the shapes
for side in range (4):
    pen.forward(100)
    pen.left(90)

# While loop that executes three times
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)  
    sides = sides - 1 




# Wait for user to close window
win.mainloop()