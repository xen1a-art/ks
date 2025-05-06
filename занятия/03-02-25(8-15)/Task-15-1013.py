from itertools import combinations

def f(x):
    P = 23 <= x <= 45
    Q = 34 <= x <= 56
    A = A1 <= x <= A2
    return (not A) or (not P) and Q

ans = []
line = [i/10 for i in range(0*10,70*10)]

for A1,A2 in combinations(line,2):
    if all(f(x)== 1 for x in line):
        ans.append(A2-A1)
print(max(ans))