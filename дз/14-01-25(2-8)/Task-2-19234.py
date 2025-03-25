print('w x y z')
for w in 0,1:
    for x in 0,1:
        for y in 0, 1:
            for z in 0, 1:
                f = (not(((not x) or y ) and (not w)) ) or (not(z and (not(y and w))))
                if not f:
                    print(w,x,y,z)