# Если в задании просят найти самое длинное число, кратное N,
# то мы должны помнить, что внутри каждой неподходящей подстроки,
# может скрываться более короткая подстрока, которая подойдет под условие

from string import ascii_uppercase

with open('24_9791.txt') as file:
    data = file.readline()

for i in ascii_uppercase[6:]:
    data = data.replace(i, ' ')

data = data.split()

# Определите длину самой длинной подстроки,
# являющейся 16-ричным числом,
# которое делится на 3 без остатка

ans = []
for i in data:
    st = i.lstrip('0') # Убираем ведущие нули
    # Проверяем, подходит ли самая большая строка под условие
    if int(st, 16) % 3 == 0:
        ans.append(len(st))
    else:
        # Перебираем все подстроки текущей строки
        for l in range(len(st)):
            for r in range(len(st), l, -1):
                sub_st = st[l:r].lstrip('0')
                if int(sub_st, 16) % 3 == 0:
                    ans.append(len(sub_st))
                    break

print(max(ans))