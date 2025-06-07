def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(1) == 2 and cnt.count(4) == 1
def f2(nums):
    nepov = [i for i in set(nums) if nums.count(i) == 1 ]
    pov = [i for i in nums if nums.count(i) > 1]
    return pov[0] >= sum(nepov) / len(nepov)

with open('09_9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1 and f2 :
        cnt += 1
print(cnt)
