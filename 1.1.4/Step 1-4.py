#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.forward(50)
painter.right(90)
painter.pendown()
painter.pensize(20)
painter.turtlesize(8)
painter.shape("triangle")

# Add a loop with a zero-iteration condition
start_loop = 'start'

while start_loop == 'start':
    painter.color("midnightblue")
    painter.stamp()
    painter.color("orange")
    painter.forward(10)
    painter.color("violet")
    painter.circle(40, 140, 40)
    painter.color("yellow")
    painter.right(50)
    painter.color("purple")
    painter.forward(50)
    painter.color("brown")
    painter.right(10)
    painter.color("cyan")
    painter.backward(100)
    painter.circle(200,73,4)

# Add an infinite loop


wn = trtl.Screen()
wn.mainloop()