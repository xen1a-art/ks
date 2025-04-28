from turtle import *

tracer(0)
screensize(10_000,10_000)
m = 12


rt(45)
for i in range(10):
    rt(45)
    fd(203*m)
    rt(45)
up()
bk(40*m)
rt(45)
down()
for i in range(5):
    fd(20*m)
    lt(90)
up()
for x in range(-250,-100):
    for y in range(-250, -100):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()

