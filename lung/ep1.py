import turtle

# Create a Turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(10)

#Set the fill color of the shapes
t.fillcolor("purple")

#Begin filling the shapes
t.begin_fill()

#Draw the pattern
for i in range(36):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

# End filling the shapes
t.end_fill()

# Exit the turtle window
turtle.done()


























