t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    # if the alternating subsequence starts with positive number
    st_ind = None
    for i, num in enumerate(nums):
        if num > 0:
            st_ind = i
            break
    
    turn = 0
    alt_sub_1 = []

    if st_ind != None:
        for i in range(st_ind, n):
            cur = nums[i]
            if turn == 0:
                if cur > 0:
                    alt_sub_1.append(cur)
                    turn = 1 - turn
                
                elif alt_sub_1 and alt_sub_1[-1] < cur:
                    alt_sub_1.pop()
                    alt_sub_1.append(cur)
            
            else:
                if cur < 0:
                    alt_sub_1.append(cur)
                    turn = 1 - turn
                
                elif alt_sub_1 and alt_sub_1[-1] < cur:
                    alt_sub_1.pop()
                    alt_sub_1.append(cur)

    # if the alternating subsequence starts with negative number
    st_ind = None
    for i, num in enumerate(nums):
        if num < 0:
            st_ind = i
            break
    
    turn = 1
    alt_sub_2 = []

    if st_ind != None:
        for i in range(st_ind, n):
            cur = nums[i]
            if turn == 0:
                if cur > 0:
                    alt_sub_2.append(cur)
                    turn = 1 - turn
                
                elif alt_sub_2 and alt_sub_2[-1] < cur:
                    alt_sub_2.pop()
                    alt_sub_2.append(cur)
            
            else:
                if cur < 0:
                    alt_sub_2.append(cur)
                    turn = 1 - turn
                
                elif alt_sub_2 and alt_sub_2[-1] < cur:
                    alt_sub_2.pop()
                    alt_sub_2.append(cur)
        
    if len(alt_sub_1) == len(alt_sub_2):
        print(max(sum(alt_sub_1), sum(alt_sub_2)))
    
    elif len(alt_sub_2) > len(alt_sub_1):
        print(sum(alt_sub_2))
    
    else:
        print(sum(alt_sub_1))
