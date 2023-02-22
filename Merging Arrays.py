n, m = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
mergedArr = []
pointer1, pointer2 = 0, 0
 
while pointer1 < n and pointer2 < m:
    num1, num2 = array1[pointer1], array2[pointer2]
 
    if num1 < num2:
        mergedArr.append(num1)
        pointer1 += 1
    
    else:
        mergedArr.append(num2)
        pointer2 += 1
    
 
if pointer1 < n:
    mergedArr.extend(array1[pointer1:])
 
else:
    mergedArr.extend(array2[pointer2:])
 
print(*mergedArr)
