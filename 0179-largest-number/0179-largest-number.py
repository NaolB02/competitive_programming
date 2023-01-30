class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index in range(len(nums)):
            for index2 in range(len(nums) - 1, 0, -1):
                num1 = str(nums[index2])
                num2 = str(nums[index2 - 1])
                
                if int(num1 + num2) > int(num2 + num1):
                    nums[index2], nums[index2 - 1] = nums[index2 - 1], nums[index2]
        
        nums_concatenated = ''.join(map(str, nums))
        index = 0
        
        for num in nums_concatenated:
            if num == '0' and index != len(nums_concatenated) - 1:
                index += 1
            
            else:
                break
        
        return nums_concatenated[index:]