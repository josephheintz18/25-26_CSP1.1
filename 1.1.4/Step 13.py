import turtle as trtl

painter = trtl.Turtle()

painter.speed(0)

color1 = "violet"
color2 = "limegreen"
height = 300
angle = 7
space = 1

while painter.ycor() < height:
   if painter.pencolor() == color2:
       painter.fillcolor(color1)
       painter.color(color1)
   else:
       painter.fillcolor(color2)
       painter.color(color2)

   painter.right(angle)
   painter.forward(2 * space + 10) # experiment
   painter.begin_fill()
   painter.circle(3)
   painter.end_fill()
   space = space + 0.25
   if (space % 200 == 0):
        painter.fillcolor(color1)
        painter.color(color1)
   elif (space % 100 == 1):
       painter.fillcolor(color2)
       painter.color(color2)
# change color

wn = trtl.Screen()
wn.mainloop()