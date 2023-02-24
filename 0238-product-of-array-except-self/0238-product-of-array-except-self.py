class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct = [1]
        for index in range(len(nums)):
            preProduct.append(preProduct[-1] * nums[index])
        
        suffProduct = [1]
        for index in range(len(nums) - 1, -1, -1):
            suffProduct.append(suffProduct[-1] * nums[index])
        
        suffProduct.reverse()
        
        res = []
        for index in range(len(nums)):
            res.append(preProduct[index] * suffProduct[index + 1])
        
        return res