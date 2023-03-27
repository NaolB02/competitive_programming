class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        
        # merge sort with a little modification
        def merge(left_half, right_half):
            nonlocal count
            
            # find the possible pairs before merging comparing the right and left halves
            right_double = [2 * right_half[i] for i in range(len(right_half))]
            for i in range(len(left_half)):
                index = bisect_left(right_double, left_half[i])
                count += index
            
            n, m = len(left_half), len(right_half)
            left, right = n - 1, m - 1
            temp = [0] * m
            left_half += temp
            index = m + n - 1                

            while left >= 0 and right >= 0:
                if left_half[left] >= right_half[right]:
                    left_half[index] = left_half[left]
                    left -= 1

                else:
                    left_half[index] = right_half[right]
                    right -= 1

                index -= 1

            while right >= 0:
                left_half[index] = right_half[right]
                right -= 1
                index -= 1

            return left_half

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]

            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            return merge(left_half, right_half)
        
        mergeSort(0, len(nums) - 1, nums)
        return count