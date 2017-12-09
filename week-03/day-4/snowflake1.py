import turtle


def kochsnowflake(length,depth):
    if depth==0:
        t.forward(length)
    else:
        t.speed(0)
        kochsnowflake(length/3,depth-1)
        t.left(60)
        kochsnowflake(length/3,depth-1)
        t.right(120)
        kochsnowflake(length/3,depth-1)
        t.left(60)
        kochsnowflake(length/3,depth-1)



def snowflake():
    for i in range(3):
        kochsnowflake(390, 5)
        t.right(120)



t = turtle.Turtle()
hex = turtle.Screen()
hex.bgcolor('black')
turtle.hideturtle()
t._tracer(0,0)
t.color("white")
t.speed(0)
t.penup()
t.backward(200)
t.left(90)
t.forward(120)
t.right(90)
t.pendown()
snowflake()
hex.update()
hex.exitonclick()