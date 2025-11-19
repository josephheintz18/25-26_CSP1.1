import turtle as trtl
t = trtl.Turtle()

lamp = -2

#Making the cap
t.right(45)
t.penup()
t.goto(-25,55)
for cap in range(2):
    t.pendown()
    t.circle(50, 90)
    t.circle(10, 90)

#Making the see through part
for a in range(2):
    if lamp < 0:
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



wn = trtl.Screen()
wn.mainloop()