import turtle,time
turtle.bgcolor("orange")
turtle.hideturtle()
turtle.speed(0)
l=0
colors=('purple','red','white')
for i in range(55):
    for j in colors:
        turtle.pencolor(j)
        turtle.fd(l)
        turtle.right(90)
        l+=1
    turtle.right(180)
time.sleep(5)


        



