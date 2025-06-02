# #1 способ
# print('a b c d')
# for a in 0,1:
#     for b in 0, 1:
#         for c in 0, 1:
#             for d in 0, 1:
#                 f = ((not a) and (not b)) or (b == c) or d
#                 if not f:
#                     print(a,b,c,d)

from itertools import permutations, product
def f(a,b,c,d):
    return ((not a) and (not b)) or (b == c) or d
for a1,a2,a3,a4 in product([0,1], repeat = 4):
    table = [(a1,a2,1,a3),(1,0,a4,1),(0,0,1,1)]
    if len(table) == len(set(table)):
        for p in permutations('abcd'):
            u = [f(**dict(zip(p,t))) for t in table] == [0,0,0]
            if u:
                print(*p)
