t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    while len(nums) != 1:
        if nums[-1] - nums[-2] <= 1:
            nums.pop()
        
        else:
            break
    
    if len(nums) == 1:
        print('YES')
    
    else:
        print('NO')
