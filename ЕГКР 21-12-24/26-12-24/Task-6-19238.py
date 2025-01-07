from turtle import*

tracer(0)
screensize(1000,1000)
m = 15

for i in range(8):
    fd(16* m)
    rt(90)
    fd(22* m)
    rt(90)
up()
fd(5* m)
rt(90)
fd(5* m)
lt(90)
down()
for i in range(8):
    fd(52* m )
    rt(90)
    fd(77* m)
    rt(90)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*m, y* m)
        dot(5, 'red')
update()
done()