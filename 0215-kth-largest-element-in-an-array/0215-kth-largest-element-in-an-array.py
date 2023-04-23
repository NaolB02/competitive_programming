class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quicksort(nums, 0, len(nums) - 1)[-k]
    
    def partition(self, nums, low, high):
        pivot = nums[high]
        ind = low - 1
        
        for j in range(low, high):
            if nums[j] <= pivot:
                ind += 1
                
                nums[ind], nums[j] = nums[j], nums[ind]
                
        nums[ind + 1], nums[high] = nums[high], nums[ind + 1]
        
        
        return ind + 1
    
    def quicksort(self, nums, low, high):
        if low < high:
            pivot_ind = self.partition(nums, low, high)
            
            self.quicksort(nums, low, pivot_ind - 1)
            self.quicksort(nums, pivot_ind + 1, high)
        
        return nums