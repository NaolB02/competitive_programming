class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_list = []
        
        for index in nums:
            count = 0
            
            for index2 in nums:
                if index2 < index:
                    count += 1
                    
            count_list.append(count)
            
        return count_list  