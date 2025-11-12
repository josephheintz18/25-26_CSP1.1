import turtle as trtl

# create spider body
spider = trtl.Turtle()
spider.pensize(40)
spider.pencolor('limegreen')
spider.circle(20)
spider.speed(0)
# create spider head
spider.goto(0, -30)
spider.circle(5)

# config spider legs
num_legs = 8
leg_length = 50 # reduce length
angle = 360/num_legs - 25 # reduce angle
spider.pensize(5)

# draw curved legs, use +/- extent value to change the direction of curve
leg = 0
radius = 60
while leg < num_legs:
  spider.goto(0,20)
  if leg < 4:
    spider.setheading(angle*leg + 125)
    spider.pendown()
    spider.circle(radius, 120)
    spider.penup()
  else:
    spider.setheading(angle*leg + 90)
    spider.pendown()
    spider.circle(radius, -120)
    spider.penup()

  leg = leg + 1

# draw eyes
spider.pensize(5)
spider.color("white")
spider.penup()
spider.goto(-2, -35)
spider.pendown()
spider.circle(5)
spider.penup()
spider.goto(10, -35)
spider.pendown()
spider.circle(5)

spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()