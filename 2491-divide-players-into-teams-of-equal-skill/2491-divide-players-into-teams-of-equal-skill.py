class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start, end = 0, len(skill) - 1
        target = skill[start] + skill[end]
        chemistry = 0
        
        while end > start:
            if skill[start] + skill[end] != target:
                return -1
            
            chemistry += (skill[start] * skill[end])
            start += 1
            end -= 1
        
        return chemistry            