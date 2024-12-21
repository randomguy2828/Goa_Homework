from turtle import*
#castle building
speed(20)
width(5)
color("grey")
begin_fill()
forward(300)
left(180)
forward(600)
right(90)
forward(300)
right(90)
forward(600)
right(90)
forward(300)
end_fill()

begin_fill()
penup()
goto(300,300)
pendown()
right(180)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
end_fill()

begin_fill()
penup()
goto(-300,300)
pendown()
left(180)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()
#--------------------------------------------------------------------------------
#door
penup()
goto(-75,0)
pendown()
color("brown")
begin_fill()
left(180)
forward(180)
right(90)
forward(150)
right(90)
forward(180)
end_fill()
#--------------------------------------------------------------------------------
#road to castle
color("black")
begin_fill()
forward(500)
right(90)
forward(150)
right(90)
forward(500)
end_fill()
#-------------------------------------------------------------------------------
#grass
color("green")
begin_fill()
left(90)
forward(880)
left(90)
forward(500)
left(90)
forward(880)
left(90)
forward(500)
end_fill()

penup()
goto(75,0)
pendown()
begin_fill()
right(90)
forward(880)
right(90)
forward(500)
right(90)
forward(880)
right(90)
forward(500)
end_fill()

#--------------------------------------------------------------------------------
#king
penup()
goto(-100,300)
pendown()
color("yellow")
begin_fill()
forward(120)
right(90)
forward(50)
right(90)
forward(120)
right(90)
forward(50)
right(90)
end_fill()
begin_fill()
forward(120)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
end_fill()
begin_fill()
forward(50)
right(90)
forward(80)
right(90)
forward(50)
right(90)
forward(30)
right(90)
end_fill()
begin_fill()
forward(100)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#-------------------------------------------------------------------------------------
#queen
penup()
goto(100,300)
pendown()
color("red")
begin_fill()
right(160)
forward(140)
left(140)
forward(140)
left(110)
forward(100)
end_fill()
penup()
goto(30,430)
pendown()
begin_fill()
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()















































exitonclick()