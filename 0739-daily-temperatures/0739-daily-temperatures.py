class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        monStack = []
        
        for i, tem in enumerate(temperatures):
            while monStack and monStack[-1][1] < tem:
                ind, curTemp = monStack.pop()
                answer[ind] = i - ind
            monStack.append([i, tem])
        
        return answer
            