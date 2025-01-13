from itertools import product, permutations

def f(x,y ,w, z):
    return ((x and (not y )) or (x == z) or w)

for a1,a2,a3,a4  in product([1,0], repeat = 4):
    table = [(a1,a2,0,1),(1,0,a3,1), (1,1,0,a4)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            u = [f(**dict(zip(p, t))) for t in table ] == [0,0,0]
            if u:
                print(*p)
