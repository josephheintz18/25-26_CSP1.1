import turtle as trtl
t = trtl.Turtle()

t.speed(0)
lamp = 0
xcor = 0
ycor = 0
xcor2 = -20
ycor2 = -80

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
t.right(-240)
t.circle(-87, -95)
t.penup()
t.right(48)
t.forward(127)
t.right(-75)
t.pendown()
t.forward(50)
t.right(-107)
t.right(-130)
t.circle(-100, -100)
t.right(123)
t.forward(45)
t.right(24)
t.forward(65)

#The lava
t.penup()
t.forward(5)
t.right(60)
t.forward(-9)
t.pendown()
t.pensize(12)
t.pencolor('orange')
t.right(-80)
t.forward(145)
t.right(-120)
t.circle (-50, 88)
t.right(-123)
t.forward(142)
t.right(-57)
t.circle(100,82)
t.right(220)
t.forward(30)
t.pensize(40)
t.forward(70)
t.right(90)
t.forward(117)
t.right(90)
t.forward(46)
t.right(90)
t.forward(40)
t.pensize(60)
t.forward(75)
t.pensize(60)
t.right(-150)
t.forward(35)
t.pensize(50)
t.right(140)
t.forward(30)
t.forward(-100)

for q in range(3):
    t.penup()
    t.shape('circle')
    t.color('darkorange')
    t.goto(xcor, ycor)
    t.pendown()
    t.stamp()
    if xcor > 10:
        t.penup()
        t.color('yellow')
        t.goto(xcor2, ycor2)
        t.shapesize(2.5)
        t.stamp()
    elif xcor == 0:
        t.color('yellow')
        t.shapesize(1.5)
        t.stamp()

    xcor += 20
    ycor += -30



wn = trtl.Screen()
wn.mainloop()