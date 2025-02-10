from itertools import combinations

def f(x):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = A1 <= x <= A2
    return (not (C or J)) <= (not A)

ans = []
line = [i/10 for i in range(46*10, 102*10)]
for A1,A2 in combinations(line, 2):
    if all(f(x) ==1 for x in line):
        ans.append(A2-A1)
print(max(ans))