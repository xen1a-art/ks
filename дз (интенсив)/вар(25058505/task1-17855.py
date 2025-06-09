from itertools import permutations

matrix = '457 46 567 12 136 235 13'.split()
graph = 'EC CA AB BD DF FE GF GD GC'.split()
print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)