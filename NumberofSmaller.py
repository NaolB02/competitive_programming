n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
countingArr = []
pointer1 = 0
 
for pointer2 in range(m):
    while pointer1 < n and  arr1[pointer1] < arr2[pointer2]:
        pointer1 += 1
    
    countingArr.append(pointer1)
 
print(*countingArr)
