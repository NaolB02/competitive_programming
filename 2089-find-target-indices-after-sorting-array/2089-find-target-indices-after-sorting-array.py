class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)
        answer = []
        for i in range(n):
            if nums[i] == target:
                answer.append(i)
        return answer