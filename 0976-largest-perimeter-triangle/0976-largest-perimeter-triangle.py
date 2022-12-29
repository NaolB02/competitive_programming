class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxPerimeter = 0
        n = len(nums)
        right = n - 1
        left = right - 2
        nums.sort()
        
        while left >= 0:
            curPerimeter = sum(nums[left: right + 1])
            
            # checking if the triplet can form a triangle
            if nums[left] + nums[left + 1] > nums[right]:
                maxPerimeter = max(maxPerimeter, curPerimeter)
            
            left -= 1
            right -= 1
        
        return maxPerimeter