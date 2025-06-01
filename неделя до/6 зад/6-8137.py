from turtle import *

tracer(0)
screensize(600,600)
m = 10

rt(90)
for i in range(7):
    fd(11*m)
    rt(45)
    fd(8*m)
    rt(135)
up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()