class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        equal = []
        less = []
        
        for num in nums:
            if num > pivot:
                greater.append(num)
            
            elif num == pivot:
                equal.append(num)
            
            else:
                less.append(num)
        
        total = less + equal + greater
        for index in range(len(total)):
            nums[index] = total[index]
        
        return nums