def f(cur,end):
    if cur == end: return 1
    if cur > end: return 0
    if cur < end: return f(cur + 1,end) + f(cur *2, end) + f(cur *2 + 1,end)
print(f(4,29))