def f(cur,end):
    if cur == end: return 1
    if cur > end or cur == 21: return False
    return f(cur + 2,end) + f(cur + 3, end) + f(cur * 2, end)
print(f(7,14)*f(14,32))