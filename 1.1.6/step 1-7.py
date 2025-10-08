#   a116_buggy_image.py
import turtle as trtl
from operator import length_hint
from sys import builtin_module_names

# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

#drawing the spider's body
spider.speed(0)
spider.pensize(40)
spider.pencolor('limegreen')
spider.penup()
spider.goto(0, 0)
spider.forward(20)
spider.left(90)
spider.pendown()
spider.circle(20)

#configuring the spider's legs
num_of_legs = 8
length_of_leg = 70
angle = 360 / num_of_legs
spider.pensize(5)
num_legs_fin = 4

#drawing the spider's legs
spider.speed(1)
'''
while (num_legs_fin < num_of_legs):
  spider.goto(0, 0)
  spider.setheading(35 * num_legs_fin)
  spider.forward(length_of_leg)
  num_legs_fin = num_legs_fin + 1
num_legs_fin = 4
spider.goto(0, 0)

while (num_legs_fin < num_of_legs):
  spider.goto(0, 0)
  spider.setheading(35 * num_legs_fin)
  spider.forward(length_of_leg)
  num_legs_fin = num_legs_fin + 1
'''

print(num_legs_fin)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()