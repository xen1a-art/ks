from turtle import *

tracer(0)
lt(90)
up()
screensize(1000,1000)
m = 10

for i in range(2):
    down()
    for i in range(2):
        fd(8 * m)
        rt(90)
        fd(8 * m)
        rt(90)
    up()
    fd(6 * m)
    rt(90)
    fd(6 * m)
    lt(90)
rt(180)
fd(4 * m)
down()
for i in range(4):
    fd(8 * m)
    rt(270)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(5, 'red')
update()
done()