# 정사각형 그리기
import turtle

for i in range(4):
    turtle.forward(50)
    if i == 3:
        break
    turtle.right(90)

turtle.exitonclick()    