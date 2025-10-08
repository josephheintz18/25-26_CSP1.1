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

start_loop = 'start'

while start_loop == 'start':
    painter.color("maroon")
    painter.stamp()
    painter.color("yellow")
    painter.forward(10)
    painter.color("orange")
    painter.circle(40, 140, 40)
    painter.color("brown")
    painter.right(50)
    painter.color("limegreen")
    painter.forward(50)
    painter.shape("triangle")
    painter.color("red")
    painter.right(10)
    painter.color("cyan")
    painter.backward(100)
    painter.circle(200,73,4)

wn = trtl.Screen()
wn.mainloop()