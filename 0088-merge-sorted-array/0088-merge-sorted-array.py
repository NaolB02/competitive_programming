class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1.copy()
        i = j = k = 0
        
        while i < m and j < n:
            if temp[i] <= nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
            
        if i < m:
            for l in range(i, m):
                nums1[k] = temp[l]
                k += 1
        else:
            for l in range(j, n):
                nums1[k] = nums2[l]
                k += 1
            
            
        