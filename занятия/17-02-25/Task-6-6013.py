from turtle import *

tracer(0)
screensize(1000,1000)
lt(90)
m = 10

for i in range(2):
    rt(120)
    fd(7*m)
rt(300)
for i in range(2):
    rt(120)
    fd(7*m)
up()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x *m, y * m)
        dot(3, 'red')
update()
done()