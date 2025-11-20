import turtle as trtl
t = trtl.Turtle()
t.speed(0)

lamp = 0

#Cap
t.right(45)
t.penup()
t.goto(-25,55)
for cap in range(2):
    t.pendown()
    t.circle(50, 90)
    t.circle(10, 90)

#The lamp
for a in range(2):
    if lamp < 1:
        t.right(55)
        t.penup()
        t.goto(-28, 60)
        t.pendown()
        t.forward(160)
    elif lamp > 0:
        t.penup()
        t.goto(50, 59)
        t.right(-25)
        t.pendown()
        t.forward(160)
    lamp +=5
t.penup()
t.goto(-56,-96)
t.right(-206)
t.pendown()
t.circle(-97, -99)

#Lamp Base
t.penup()
t.goto(-56,-96)
t.pendown()
t.right(-53)
t.forward(65)
t.right(30)
#yk yk
t.right(-107)
t.forward(150)
t.penup()
t.forward(-150)
t.right(107)
#yk yk
t.pendown()
t.forward(65)
t.right(-107)
t.pendown()
t.right(-130)
t.circle(-100, -100)
t.right(135)
t.forward(65)

wn = trtl.Screen()
wn.mainloop()