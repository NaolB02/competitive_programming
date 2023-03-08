class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        
        start_end = []
        
        # find starting position
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] >= target:
                high = mid - 1
            
            else:
                low = mid + 1
        
        if low == len(nums) or nums[low] != target:
            start_end.append(-1)
        
        else:
            start_end.append(low)
        
        # find ending position
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] > target:
                high = mid - 1
            
            else:
                low = mid + 1
        
        low -= 1
        if low == len(nums) or nums[low] != target:
            start_end.append(-1)
        
        else:
            start_end.append(low)
    
        return start_end
        