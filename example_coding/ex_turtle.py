import turtle

scr = turtle.Screen()
scr.bgcolor("yellow")
turtle.pensize(3)

# for i in range(0,10):
#     turtle.right(36)
#     for j in range(0,5):
#         turtle.forward(100)
#         turtle.right(72)
# turtle.exitonclick()

for i in range(0,10):
    turtle.right(36)
    for j in range(0,4):
        turtle.begin_fill()
        turtle.forward(50)
        turtle.right(72)    