def f(cur,end):
    if cur == end: return  1
    if cur < end : return 0
    return f(cur -2,end) + f(cur//2, end)
print(f(30,14)*f(14,1))
