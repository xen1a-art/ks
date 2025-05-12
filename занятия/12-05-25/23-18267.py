def f(cur,end,R):
    if cur == end and R == True : return 1
    if cur > end: return 0
    return f(cur + 2,end,True) + f(cur + 5,end,True) + f(cur ** 2,end,False)
print(f(4,36,0))