class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        monoStack = []
        
        if len(num) == k:
            return "0"

        for i in range(len(num)):
            while k > 0 and monoStack and monoStack[-1] > num[i]:
                monoStack.pop()
                k -= 1
        
            monoStack.append(num[i])
        
        if k:
            monoStack = monoStack[0: -k]
        
        return str(int("".join(monoStack)))