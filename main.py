import turtle
import random

#Change the background color to black
turtle.bgcolor("black")

#Adjust speed of Turtle (lower=faster)
turtle.speed(0)

#List of colors
colors=["#00ff9f","#00b8ff","#001eff","#bd00ff","#fcee0c"]

#Counter variables

colorNum=0
size=1

#Change this variable to control how many sides your shape will have
sides=4

#Draw the spiraling shape
#This loops forever
while(True):
  colorNum=colorNum+1
  for i in range(sides):
    turtle.forward(size)
    turtle.right(360/sides+2)
    size=size+1
  turtle.color(colors[colorNum%5])
    