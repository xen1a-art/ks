from turtle import *

tracer(0)
screensize(1000,1000)
lt(90)
m = 15

for i in range(7):
    fd(10*m)
    rt(120)
up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()