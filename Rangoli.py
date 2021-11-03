import turtle as t
import random

tom=t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def location(angle): #Drawing Small circles
    tom.penup()
    tom.goto(0,0)
    tom.setheading(angle)
    tom.forward(200)
    tom.pendown()
    tom.setheading(angle)
    tom.color("black", "#d902ee")
    tom.begin_fill()
    tom.circle(30)
    tom.end_fill()
    
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        #setheading makes turtle headed at a particular angle i.e size_of_gap here
        tom.color(random_color())
        tom.circle(100)
        current_heading = tom.heading()
        tom.setheading(current_heading+size_of_gap)

def mini(x,y): #Drawing 4 big Circles
    tom.penup()
    tom.goto(x,y)
    tom.pendown()
    tom.color("black", "#FE8447")
    tom.begin_fill()
    tom.circle(60)
    tom.end_fill()

tom.speed("fastest")

draw_spirograph(5)

mini(0,-60)
mini(0,200)
mini(0,-320)
mini(-260,-60)
mini(260,-60)

location(-7.5)
location(22.5)
location(52.5)
location(82.5)
location(112.5)
location(142.5)
location(172.5)
location(-37.5)
location(-67.5)
location(-97.5)
location(-127.5)
location(-157.5)

#Center Small Cicle
tom.penup()
tom.goto(0,-30)
tom.setheading(0)
tom.color("black", "#d902ee")
tom.begin_fill()
tom.circle(30)
tom.end_fill()

screen = t.Screen()
screen.exitonclick()
    
