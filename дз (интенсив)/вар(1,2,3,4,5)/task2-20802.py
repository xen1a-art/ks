#1способ
# from itertools import permutations, product
# def f(w,x,y,z):
#     return (w <= (not (z <= x))) or y
#
# for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat = 7):
#     table = [(1,a1,a2,a3),
#              (0,1,0,a4),
#              (a5,0,a6,a7)]
#     if len(table) == len(set(table)):
#         for p in permutations('wxyz'):
#             u = [f(**dict(zip(p,t))) for t in table] == [0,0,0]
#             if u:
#                 print(*p)

#2способ
print('w x y z')
for w in 0,1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = (w <= (not (z <= x))) or y
                if not f:
                    print(w,x,y,z)