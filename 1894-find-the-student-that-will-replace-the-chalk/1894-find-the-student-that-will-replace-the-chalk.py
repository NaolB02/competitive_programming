class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        preSum = 0
        for i in range(len(chalk)):
            preSum += chalk[i]
        
        val = k % preSum
        
        while val > preSum:
            val = val % preSum
        
        for i in range(len(chalk)):
            if val < chalk[i]:
                return i
            val -= chalk[i]