import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("#FEFBF6")
t.pencolor("black")
t.speed(3)

t.color("#e82127")
t.penup()
t.goto(-160,160)
t.pendown()

t.begin_fill()
t.left(18)
t.circle(-500,40)
t.right(90)
t.forward(17)
t.right(89.5)
t.circle(500,39)
t.right(90)
t.forward(17)
t.end_fill()

t.penup()
t.goto(-155,133)
t.pendown()
t.begin_fill()
t.right(90.5)
t.circle(-500,38)
t.right(70)
t.circle(-30,80)
t.left(90)
t.circle(-20,-70)
t.right(10)
t.circle(-300,-15)
t.right(93)
t.forward(280)
t.right(160)
t.forward(280)
t.left(80)
t.circle(300,15)
t.circle(20,70)
t.left(80)
t.circle(30,-80)
t.end_fill()
t.penup()
t.goto(-20,155)
t.pendown()
t.pencolor("black")
t.color("#FEFBF6")
t.begin_fill()
t.left(30)
t.forward(60)
t.left(130)
t.forward(65)
t.end_fill()

# T
t.pencolor("#e82127")
t.penup()
t.goto(-200,-210)
t.pendown()
t.right(66)
t.pensize(10)
t.forward(60)
t.back(30)
t.right(90)
t.forward(70)

# E
t.penup()
t.goto(-115, -210)
t.pendown()
t.left(90)
t.forward(60)
t.penup()
t.goto(-115, -245)
t.pendown()
t.forward(60)
t.penup()
t.goto(-115, -280)
t.pendown()
t.forward(60)
t.penup()
t.goto(-115, -280)
t.pendown()
t.forward(60)

# S
t.penup()
t.goto(-20, -210)
t.pendown()
t.forward(60)
t.backward(60)
t.right(90)
t.forward(34)
t.left(90)
t.forward(60)
t.right(90)
t.forward(34)
t.right(90)
t.forward(60)

# L
t.penup()
t.goto(70, -210)
t.pendown()
t.left(90)
t.forward(70)
t.left(90)
t.forward(60)

# A
t.penup()
t.goto(155, -210)
t.pendown()
t.forward(60)
t.penup()
t.goto(150, -280)
t.pendown()
t.left(90)
t.forward(32.5)
t.right(90)
t.forward(60)
t.right(90)
t.forward(32.5)
t.hideturtle()

turtle.done()


















