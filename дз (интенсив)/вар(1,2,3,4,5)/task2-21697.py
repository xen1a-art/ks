from itertools import permutations, product
def f(w,x,y,z):
    return (not (x<=y)) or (z==w) or z

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat = 7):
    table = [(0,0,a1,a2),
             (a3,a4,1,a5),
             (a6,1,0,a7)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p,t))) for t in table] == [0,0,0]
            if u:
                print(*p)