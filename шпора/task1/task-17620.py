from itertools import permutations

matrix = '256 134 267 27 16 135 34'.split()
graph = 'AF FE EC CG GD DB BA ED FB'.split()
print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+ 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
#====================================================

#Если в выводе результата программы отображаются несколько строк,
#то либо вы опечатались и стоит себя перепроверить, либо граф симметричный.
#Если после перепроверки опечаток не найдено, значит граф точно симметричный