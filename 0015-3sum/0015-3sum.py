class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutionSet = []

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue
    

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    if j > i + 1 and k < len(nums) - 1 and nums[j] == nums[j - 1] and nums[k] == nums[k + 1]:
                        j += 1
                        k -= 1
                        continue
                    solutionSet.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                elif sum > 0:
                    k -= 1
                
                else:
                    j += 1
                 
        return solutionSet

