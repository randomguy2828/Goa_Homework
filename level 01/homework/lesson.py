from turtle import *
#paint house
shape("turtle")
width(7)
color("green")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#door
width(8)

forward(75)
left(90)
color("purple")
begin_fill()
forward(100)
right(90)
forward(50)
right(90)
forward(100)
left(90)
end_fill()

#roof
penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(225)
forward(140)
left(90)
forward(140)
end_fill()
#roof end

#window
penup()
goto(20, 120)
pendown()
color("yellow")
begin_fill()
left(135)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
end_fill()


#second window
penup()
goto(180, 120)
pendown()
begin_fill()
left(180)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
end_fill()













exitonclick()