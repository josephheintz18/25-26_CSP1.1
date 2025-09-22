# import the turtle module
import turtle as trtl
painter = trtl.Turtle()

# the dudes head
painter.circle(125)
painter.penup()
painter.circle(125, 100)

# Eyes
painter.left(90)
painter.forward(75)
painter.pendown()
painter.circle(40)
painter.penup()
painter.right(10)
painter.forward(100)
painter.pendown()
painter.circle(40)

# Pupils
painter.penup()
painter.left(90)
painter.forward(40)
painter.right(90)
painter.forward(5)
painter.pendown()
painter.circle(20)
painter.right(180)
painter.penup()
painter.forward(100)
painter.right(90)
painter.forward(17)
painter.pendown()
painter.circle(20)

# Mouth
painter.penup()
painter.forward(40)
painter.right(90)
painter.pendown()
painter.forward(100)

# Hair
painter.penup()
painter.forward(40)
painter.right(90)
painter.forward(90)
painter.right(65)
painter.pendown()
painter.forward(60)
painter.right(78)
painter.forward(60)
painter.left(90)
painter.forward(70)
painter.right(67)
painter.forward(60)
painter.left(90)
painter.forward(70)
painter.left(35)
painter.circle(135, 180, 5)

wn = trtl.Screen()
wn.mainloop()