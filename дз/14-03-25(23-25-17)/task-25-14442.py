from fnmatch import *

def divs(num):
    d = set()
    for div in range(1,int(num**0.5)+1):
        if num % div == 0:
            d.add(div)
            d.add(num//div)
    return [x for x in d if fnmatch(str(x),'*7?')]

for n in range(400_000,500_001):
    if len(divs(n)) >= 18:
        print(n,sum(divs(n)))
