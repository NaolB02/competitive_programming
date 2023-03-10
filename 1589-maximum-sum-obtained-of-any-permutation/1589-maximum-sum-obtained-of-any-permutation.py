class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # min_val = min(request, key = lambda x: x[0])
        # max_val = max(request, key = lambda x: x[1])
        freq = [0] * len(nums)
        
        for start, end in requests:
            freq[start] += 1
            if end + 1 < len(nums):
                freq[end + 1] -= 1
        
        for index in range(1, len(freq)):
            freq[index] += freq[index - 1]
        
        for i in range(len(freq)):
            val = freq[i]
            freq[i] = [val, i]
        
        freq.sort()
        
        copy_nums = nums.copy()
        copy_nums.sort()
        j = len(freq) - 1
        for i in range(len(copy_nums) - 1, -1, -1):
            req_ind = freq[j][1]
            nums[req_ind] = copy_nums[i]
            j -= 1
        
        pre_sum = [0]
        
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
        
        max_sum = 0
        for start, end in requests:
            max_sum += pre_sum[end + 1] - pre_sum[start]
        return max_sum % (10 ** 9 + 7)