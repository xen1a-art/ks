print('w x z y')
for w in 0,1:
    for x in 0, 1:
        for z in 0, 1:
            for y in 0, 1:
                f = (x <= (y and (not z))) or w
                if not f:
                    print(w,x,z,y)
