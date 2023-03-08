class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_divisor = max(nums)
        low, high = 1, max_divisor
        
        while low <= high:
            mid = low + (high - low) // 2
            res = 0
            
            for num in nums:
                res += ceil(num / mid)
            
            if res <= threshold:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return low