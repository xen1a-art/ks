from itertools import combinations

def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = A1 <= x <= A2
    return (Q <= (not R)) and A and (not P)

ans = []
line = [i/10 for i in range(8*10,42*10)]

for A1,A2 in combinations(line,2):
    if all(f(x) == 0 for x in line):
        ans.append(A2-A1)
print(max(ans))