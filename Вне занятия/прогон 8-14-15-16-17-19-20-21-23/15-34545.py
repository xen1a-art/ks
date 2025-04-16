from itertools import combinations

def f(x):
    P = 12 <= x <= 62
    Q = 32 <= x <= 92
    A = a1 <= x <= a2
    return ((not A) and Q) <= P

ans = []
line = [i/10 for i in range(10*10,94*10)]
for a1,a2 in combinations(line,2):
    if all(f(x) == 1 for x in line):
        ans.append(a2-a1)
print(min(ans))