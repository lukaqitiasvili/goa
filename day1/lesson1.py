from turtle import *


#we want to paint a house


#step 1:  drow a spuare
speed(30) 
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drowing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #heigt qf the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drowing a windows
penup()
goto(200,120)
pendown()
color("green")
begin_fill()
right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(200, 200)
pendown()
color("purple")
right(90)
forward(200)
left(90)
forward(80)
color("green")
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
penup()



exitonclick()

