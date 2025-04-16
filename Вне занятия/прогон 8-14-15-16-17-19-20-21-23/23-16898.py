def f(cur,end):
    if cur == end: return 1
    if cur > end or cur == 5 or cur == 10: return 0
    return f(cur + 1,end) + f(cur *2,end) + f(cur + 3,end)
print(f(2,14))
