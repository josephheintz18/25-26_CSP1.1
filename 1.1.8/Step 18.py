# CODE TO COPY
#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "green", "salmon", "indigo", "brown"]

turtlocation = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, turtlocation)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-turtlocation, 350)
    vt.setheading(270)

    turtlocation += 50
distance = 3
pixel_size = 30
# TODO: move turtles across and down screen, stopping for collisions

for step in range(20):
    # For each vertical tutle
    for vt in vert_turtles:
        for ht in  horiz_turtles:
            ht.forward(distance)
            vt.forward(distance)
            distance +=2
            if distance > 10:
                distance -=4
            if abs(ht.xcor() - vt.xcor()) < pixel_size:
                if abs(ht.ycor() - vt.ycor()) < pixel_size:
                    new_shape = turtle_shapes.pop
                    vt.forward(-20)
                    ht.forward(-20)
for turtle in horiz_turtles:
    turtle.setcolor("violet")
for turtle in vert_turtles:
    turtle.setcolor("violet")

wn = trtl.Screen()
wn.mainloop()