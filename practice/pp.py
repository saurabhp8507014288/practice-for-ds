import turtle
import pyttsx3

# Set background
sc = turtle.Screen()
sc.bgcolor("skyblue")

# Bottom Line
turtle.penup()
turtle.goto(-170,-180)
turtle.color("red")
turtle.pendown()
turtle.forward(350)

# Mid Line
turtle.penup()
turtle.goto(-160,-150)
turtle.color("red")
turtle.pendown()
turtle.forward(300)

# Top Line
turtle.penup()
turtle.goto(-150,-120)
turtle.color("red")
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)

# Decoration
colors=["red","orange","yellow","green","blue","purple","black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()
for i in colors:
    angle=360/len(colors)
    turtle.color(i)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

# Birthday Message
turtle.penup()
turtle.goto(-150,50)
turtle.color("red")
turtle.pendown()
turtle.write("HAPPY BIRTHDAY ANSHIKA \U0001F600",font=("Calibri",30,"bold"))
turtle.color("black")

#wishing
eg=pyttsx3.init()
msg1="Happy birthday anshika"
msg2="may god full fill all your wishes and you live happy and  healthy life"
eg.say(msg1)
eg.say(msg2)
eg.runAndWait()
turtle.exitonclick()
