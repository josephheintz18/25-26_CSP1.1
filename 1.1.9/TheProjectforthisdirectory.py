import turtle as trtl
t = trtl.Turtle()

lamp = 0
t.speed(0)
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

#Lamp Base
t.goto(-32,-120)
t.right(-154)
t.circle(-100, -100)

wn = trtl.Screen()
wn.mainloop()