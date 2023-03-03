t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    low, high = 1, a + b
    
    while low <= high:
        mid = low + (high - low) // 2

        if mid * 4 > a + b:
            high = mid - 1
        
        else:
            low = mid + 1
    
    temp = high

    if min(a, b) >= temp:
        res = temp

    else:
        res = min(a, b)
    print(res)
