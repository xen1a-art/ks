from turtle import *

tracer(0)
screensize(500,500)
m = 10
rt(90)

up()
for i in range(10):
    rt(120)
    fd(10*m)
down()
for i in range(7):
    fd(15*m)
    rt(90)
    for i in range(5):
        rt(60)
        fd(20*m)
        rt(30)
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()
