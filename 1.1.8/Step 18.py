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
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)

    tloc += 50
distance = 3
pixel_size = 20
# TODO: move turtles across and down screen, stopping for collisions

for step in range(50):
    # For each vertical tutle
    for vt in vert_turtles:
        for ht in  horiz_turtles:
            ht.forward(distance)
            vt.forward(distance)
            distance +=1
            if distance > 6:
                distance -=1
            if abs(ht.xcor() - vt.xcor()) < pixel_size:
                if abs(ht.ycor() - vt.ycor()) < pixel_size:
                    ht.fillcolor("grey")
                    horiz_turtles.remove(ht)
                    vt.fillcolor("grey")
                    vert_turtles.remove(vt)


wn = trtl.Screen()
wn.mainloop()