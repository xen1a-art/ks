from itertools import product, permutations, repeat

def f(w, x, y, z):
    return (not(((not x) or y ) and (not w))) or (not( z and (not(y and w))))

for a1, a2, a3, a4, a5, a6, a7 in product([1,0], repeat = 7):
    table = [(0,a1,a2,1), (a3,1,a4,a5), (1,0,a6,a7)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            u= [f(**dict(zip(p,t))) for t in table] == [0,0,0]
            if u:
                print(*p)