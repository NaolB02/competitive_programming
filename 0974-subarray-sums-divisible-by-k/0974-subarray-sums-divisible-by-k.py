class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remDict = defaultdict(int)
        remDict[0] += 1
        count = 0
        pre = 0
        
        for num in nums:
            pre += num
            count += remDict[pre % k]
            remDict[pre % k] += 1
            
        return count