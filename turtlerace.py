import random
import turtle 
import time 

turtle.Turtle()
wn = turtle.Screen()
wn.setup(width = 500, height = 500)
wn.bgcolor("beige")
wn.title("Turtle Race")

def main(): 
  turtle.speed(0)
  turtle.penup()
  turtle.hideturtle()
  turtle.goto(-160,10)
  turtle.write("Starting Line")
  turtle.pendown()
  turtle.left(90)
  turtle.forward(200)
  turtle.penup()
  turtle.goto(180,10)
  turtle.pendown()
  turtle.forward(200)
  turtle.write("Finish Line")
  time.sleep(1)
  shape()

finishLineX= 55
def shape():
  red = turtle.Turtle()
  red.color("red")
  red.shape("turtle")
  red.penup()
  red.goto(-160,150)
  red.pendown()


  green = turtle.Turtle()
  green.color("green")
  green.shape("turtle")
  green.penup()
  green.goto(-160, 100)
  green.pendown()

  blue = turtle.Turtle()
  blue.color("blue")
  blue.shape("turtle")
  blue.penup()
  blue.goto(-160,50)
  blue.pendown()
  
  turtle.penup()
  turtle.goto(0,200)
  time.sleep(1)
  turtle.write("START!!!", align="center")
  
  while red.xcor() <= 200 and green.xcor() <= 200 and blue.xcor() <= 200 :
    red.forward(random.randint(1,5))
    green.forward(random.randint(1,5))
    blue.forward(random.randint(1,5))

  if red.xcor() > green.xcor() and red.xcor() > blue.xcor(): 
    print("Red Wins!!!")
  elif green.xcor() > red.xcor() and green.xcor() > blue.xcor():
    print("Green Wins!!!")
  else:
    print("Blue Wins!!!")

