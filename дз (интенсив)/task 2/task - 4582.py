from itertools import permutations, product
def f(w,x,y,z):
    return (not (w <= z)) or (x <= y) or (not x)

for a1,a2,a3,a4,a5,a6,a7 in product([0,1],repeat = 7):
    table = [(1,a1,a2,a3),
             (0,1,0,a4),
             (a5,0,a6,a7)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p,t))) for t in table] == [0,0,0]
            if u:
                print(*p)