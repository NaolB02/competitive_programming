class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        
        for log in logs:
            if len(log) == 2 and log[0] == ".":
                pass
            
            elif log[:2] == "..":
                if steps != 0:
                    steps -= 1
            
            else:
                steps += 1
        
        return steps