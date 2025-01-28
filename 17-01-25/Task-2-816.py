print('x z y')
for x in 0, 1:
    for z in 0, 1:
        for y in 0, 1:
            f = (not( x == (y <= z)))
            if f == 0:
                print(x,z,y)
