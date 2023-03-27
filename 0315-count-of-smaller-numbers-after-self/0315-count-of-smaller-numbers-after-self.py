class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        nums = [(nums[i], i) for i in range(len(nums))]
        
        # merge sort with a little modification
        def merge(left_half, right_half):
            
            # find the possible pairs before merging comparing the right and left halves
            for i in range(len(left_half)):
                num, ind = left_half[i]
                index = bisect_left(right_half, num, key = lambda x: x[0])
                count[ind] += index
            
            n, m = len(left_half), len(right_half)
            left, right = n - 1, m - 1
            temp = [0] * m
            left_half += temp
            index = m + n - 1                

            while left >= 0 and right >= 0:
                if left_half[left][0] >= right_half[right][0]:
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