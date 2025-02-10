from itertools import permutations

alph = 'хочу в вуз.'
count = 0

for i in set(permutations(alph,11)):
    i = ''.join(i)
    dd = i.split()# split -разбиение строки на список подстрок
    if len(dd) == 3 and i[-1] == '.' and i[-2] != ' ' and all( word[0] != 'у' for word in dd):
        count += 1
print(count-1)