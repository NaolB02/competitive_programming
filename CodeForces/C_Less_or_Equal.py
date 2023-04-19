

n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

start = nums[k - 1]
res = start

if k < n:
    end = nums[k]
    res = -1

    for i in range(start, end):
        res = i

if k == 0:
    res = -1
    
    for i in range(1, nums[0]):
        res = i

print(res)