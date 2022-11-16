# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i = 1        
        while True:
            cornum = (n + i) // 2
            gNum = guess(cornum)

            if gNum == 0:
                return cornum
            
            elif gNum == 1:
                i = cornum + 1
            
            elif gNum == -1:
                n = cornum - 1
            
