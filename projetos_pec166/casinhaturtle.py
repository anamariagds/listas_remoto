from turtle import *

shape("turtle")
speed(7)
#teto1
color("#DAA520")
pensize(7)
for t in range(3):
    left(120)
    forward(150)
    
right(90)
penup()
forward(10)
pendown()
color("#6A5ACD")
#base1
for q in range(4):
    forward(150)
    right(90)

left(90)
penup()
forward(10)
pendown()
color("#C71585")
#base2
for rt in range(4):
    forward(150)
    right(90)

left(90)
penup()
forward(10)
pendown()
color("#A0522D")

#teto2
left(30)
forward(150)
right(120)
forward(150)
right(60)
forward(150)
right(120)
forward(150)
done()
