print ('x y w z')
for x in (0,1):
    for y in (0,1):
        for w in (0,1):
            for z in (0,1):
                f = (x or (not y )) and (not (x == z )) and w
                if f == 1:
                    print(x, y, w, z)
