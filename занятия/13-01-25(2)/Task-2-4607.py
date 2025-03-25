from itertools import product, permutations

def f(x, y, z, w):
    return ((x <= z) <= y) or (not w)

for a1,a2,a3,a4,a5,a6,a7 in product([1,0], repeat = 7):
    table = [(1,0,a1,a2), (a3, 1, 0, a4), (0, a5, a6, a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t)))for t in table] == [0,0,0]
            if u:
                print(*p)