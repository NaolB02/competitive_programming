class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(':')', '[':']', '{':'}'}
        stack = []
        
        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if stack and char == hashmap[stack.pop()]:
                    continue
                return False
        if len(stack) != 0:
            return False
        return True