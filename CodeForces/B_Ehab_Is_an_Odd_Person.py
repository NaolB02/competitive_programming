n = int(input())
nums = list(map(int, input().split()))

even_in, odd_in = False, False
for num in nums:
    if num % 2:
        odd_in = True
    
    else:
        even_in = True

if odd_in and even_in:
    nums.sort()

print(*nums)