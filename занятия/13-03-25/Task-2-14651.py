print('x y z w')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((z <= x) == ((w <= y) or (x and w)))
                if f == 0:
                    print(x,y,z,w)