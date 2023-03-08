class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 1, len(arr) - 2
        
        while low <= high:
            mid = low + (high - low) // 2
            mid_element = arr[mid]
            
            if mid_element > arr[mid - 1] and mid_element > arr[mid + 1]:
                return mid
            
            elif mid_element > arr[mid - 1]:
                low = mid + 1
            
            else:
                high = mid - 1
                        