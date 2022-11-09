class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        preSum = defaultdict(lambda: 0)
        preSum[0] = 1
        zeroOne = []
        count = 0
        curSum = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                zeroOne.append(0)
            else:
                zeroOne.append(1)
        
        for j in range(len(zeroOne)):
            curSum += zeroOne[j]

            if curSum - k in preSum:
                count += preSum[curSum - k]
            
            preSum[curSum] += 1
            
        return count
