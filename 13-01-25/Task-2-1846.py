print ('a b c d')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                f = ((not a) and (not b)) or (b == c) or d
                if not f: #если нужны ложные значения
                    print(a, b, c, d)

                if f: #если нужны истинные значения
                    print(a, b, c, d)
                #если в таблице и 1 и 0 то без if пишем вообще