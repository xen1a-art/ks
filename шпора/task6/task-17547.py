from turtle import *

tracer(0)
screensize(2000,2000)
m = 10
lt(90)
for i in range(3):
    fd(7*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
up()
for x in range(-80,100):
    for y in range(-80, 100):
        goto(x*m,y*m)
        dot(3,"red")
update()
done()

# =============================================================
# расставление точек
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(3, 'red')