from itertools import combinations

def f(x):
    P = 35 <= x <= 55
    Q = 45 <= x <= 65
    A = A1 <= x <= A2
    return (P <= A) and ((not A) <= (not Q))

ans = []
line = [i/10 for i in range(34*10, 70*10)]
for A1,A2 in combinations(line,2):
    if all (f(x) == 1 for x in line):
        ans.append(A2-A1)
print(min(ans))
