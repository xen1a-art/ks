from itertools import combinations

def f(x):
    P = 5 <= x <= 40
    Q = 41 <= x <= 54
    R = 6 <= x <= 53
    A = A1 <= x <= A2
    return ((not P) <= Q) and R and (not A)

ans = []
line = [i/10 for i in range(4*10, 56*10)]
for A1,A2 in combinations(line,2):
    if all(f(x) == 0 for x in line):
        ans.append(A2-A1)
print(min(ans))