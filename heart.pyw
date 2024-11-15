import turtle
import json

with open('config.json') as config_file:
    config = json.load(config_file)

screen = turtle.Screen()
screen.bgcolor("black")
screen.title(config["title"])
screen.setup(width=600, height=400)

pen = turtle.Turtle()
pen.color("red")
pen.speed(1)

def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(200) 
    pen.circle(-100, 200)
    pen.left(120)
    pen.circle(-100, 200)
    pen.forward(200)
    pen.end_fill()

pen.penup()
pen.goto(0, -120)  
pen.setheading(0) 
pen.pendown()

draw_heart()

pen.penup()
pen.goto(0, 10) 
pen.color("white")
pen.pendown()
pen.write(config["name"], align="center", font=("Arial", 24, "bold"))

pen.hideturtle()
turtle.done()
