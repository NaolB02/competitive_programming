class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def isP1winner(left, right, p1 = 0, p2 = 0, turn = 0):
            if left > right:
                return p1 >= p2
            
            if not turn:
                choice1 = isP1winner(left + 1, right, p1 + nums[left], p2, 1)
                choice2 = isP1winner(left, right - 1, p1 + nums[right], p2, 1)
                return choice1 or choice2
            
            else:
                choice1 = isP1winner(left + 1, right, p1, p2 + nums[left], 0)
                choice2 = isP1winner(left, right - 1, p1, p2 + nums[right], 0)
                return choice1 and choice2
        
        return isP1winner(0, len(nums) - 1)