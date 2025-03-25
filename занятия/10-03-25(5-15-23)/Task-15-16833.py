from itertools import combinations

def f(x):
    P = 25<= x <= 73
    Q = 75 <= x <= 118
    A = A1<= x <= A2
    return (A and (not Q)) <= (P or Q)

ans = []
line = [i/10 for i in range(23*10,120*10)]

for A1,A2 in combinations(line,2):
    if all(f(x) == 1 for x in line):
        ans.append(A2-A1)

print(max(ans))
