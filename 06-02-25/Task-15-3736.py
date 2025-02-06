from itertools import combinations

def f(x):
    P = 117 <= x <= 158
    Q = 129 <= x <= 180
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

ans = []
line = [i/10 for i in range(116*10,181*10)]
for A1,A2 in combinations(line,2):
    if all(f(x) == 1 for x in line):
        ans.append(A2-A1)
print(min(ans))