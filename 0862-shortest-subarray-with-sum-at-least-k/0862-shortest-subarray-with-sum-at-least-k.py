class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        size = math.inf
        pre_sum = [0]
        
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
        
        mon_queue = deque()
        for i in range(len(pre_sum)):
            while mon_queue and pre_sum[mon_queue[-1]] >= pre_sum[i]:
                mon_queue.pop()
            
            mon_queue.append(i)
            
            while mon_queue and pre_sum[i] - pre_sum[mon_queue[0]] >= k:
                index = mon_queue.popleft()
                size = min(i - index, size)
        
        if size == math.inf:
            size = -1
        
        return size