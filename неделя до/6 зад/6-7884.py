from turtle import *

tracer(0)
screensize(5000,5000)
m = 10

rt(45)
for i in range(2):
    fd(550*m)
    rt(90)
    fd(228*m)
    rt(90)
fd(173*m)
lt(90)
fd(254*m)
rt(90)
for i in range(2):
    fd(156*m)
    rt(90)
    fd(708*m)
    rt(90)
up()
for x in range(-200,120):
    for y in range(-200, 120):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()

