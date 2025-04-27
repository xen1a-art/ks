from itertools import combinations

def f(x):
    p = 1 <= x <= 98
    q = 25 <= x <= 42
    A = A1 <=x <= A2
    return q <= ((not(p) and q) <= A)

ans = []
line = [i/10 for i in range(1*10,100*10)]
for A1,A2 in combinations(line,2):
    if all(f(x) == 1 for x in line):
        ans.append(A2-A1)
print(min(ans))