print('w y z x')
for w in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for x in 0, 1:
                f1 = (w == x ) and (y <= z )
                f2 = (w <= x) <= (y == z)
                print(w, y, z, x, f1, f2)



