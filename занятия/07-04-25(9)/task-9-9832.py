def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(1) == 2 and cnt.count(1) == 2 and cnt.count(3) == 1
def f2(nums):
    nepov = [i for i in set(nums) if nums.count(i) == 1]
    return max(nepov)

with open('9_9832.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = []
for pos,val in enumerate(data, start = 1):
    if f1 and f2:
        ans.append(sum(val),pos)