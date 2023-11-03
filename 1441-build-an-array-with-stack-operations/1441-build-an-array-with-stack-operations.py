class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        commands = []
        nums = []
        i = 1
        
        while i <= n:
            if nums and nums[-1] not in target:
                nums.pop()
                commands.append('Pop')
                continue
            
            if target == nums:
                return commands
            
            commands.append('Push')
            nums.append(i)
            i += 1
        
        return commands