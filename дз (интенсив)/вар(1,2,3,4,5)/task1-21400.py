from itertools import permutations

matrix = '457 567 45 136 123 247 126'.split()
graph = 'FA AB BG GE EF DF DA DC CE CB'.split()
print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)