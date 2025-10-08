#   a114_while_guess.py

import turtle as trtl

# modify with your two favorite colors
color1 = "limegreen"
color2 = "violet"

wn = trtl.Screen()
height = 375 # the radius of the shape

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 3
angle = 400 # experiment with the shape
seg = int(360/angle)

while (painter.ycor() < height):
  if (space % 2 == 0):
    painter.fillcolor(color1)
    painter.color(color1)
  elif (space % 2 == 1):
    painter.fillcolor(color2)
    painter.color(color2)

  painter.right(angle)
  painter.penup()
  painter.forward(2*space + 10) # experiment
  painter.pendown()
  painter.begin_fill()
  painter.circle(10)
  painter.end_fill()
  space += 1

wn.mainloop()