from itertools import permutations

alph = 'соточка'
count = 0

for i in set(permutations(alph,7)):
    i = ''.join(i)
    if i.count('оо') == 1 or i.count('оа') == 1 or i.count('аа') == 1 or i.count('ао') == 1:
        count += 1
print(count)