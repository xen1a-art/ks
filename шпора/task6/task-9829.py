from turtle import *

tracer(0)
screensize(1000,1000)
m = 10
lt(90)
rt(90)
for i in range(3):
    rt(45)
    fd(10*m)
    rt(45)
rt(315)
fd(10*m)
for i in range(2):
    rt(90)
    fd(10*m)
up()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*m,y*m)
        dot(3,"red")
update()
done()
