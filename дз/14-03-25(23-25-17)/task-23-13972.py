def f(cur,end):
    if cur == end:
        return 1
    if cur > end:
        return 0
    return (f(cur + 2,end) or f(cur * 2, end)) + f(cur + 5,end)
print(f(7,23)*f(23,35))