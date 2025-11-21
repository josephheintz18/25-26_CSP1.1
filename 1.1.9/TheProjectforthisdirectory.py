import turtle as trtl
t = trtl.Turtle()

t.speed(0)
lamp = 0
x = 0
y = 0

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
for q in range(100):
    t.penup()
    t.shape('circle')
    t.color('orange')
    t.goto(x,y)
    t.pendown()
    t.stamp()
    x+=10
    y-=30
    x = t.xcor()
    y = t.ycor()

wn = trtl.Screen()
wn.mainloop()