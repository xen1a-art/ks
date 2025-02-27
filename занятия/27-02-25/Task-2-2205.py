print('h l w n ')
for h in 0,1:
    for l in 0, 1:
        for w in 0, 1:
            for n in 0, 1:
                f = (not (h <= l)) <= ((not (w <= n)) and h )
                if not f:
                    print(h, l, w, n)
