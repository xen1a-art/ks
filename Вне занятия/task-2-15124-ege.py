from itertools import product,permutations

def f(x,y,z):
    return (x==y)or((y or z)<= x)

for a1,a2,a3 in product([0,1],repeat = 3):
    table = [(a1,1,1),(a2,a3,1)]
    if len(table) == len(set(table)):
        for p in permutations('xyz'):
            u = [f(**dict(zip(p,t))) for t in table] == [0,0]
            if u:
                print(*p)