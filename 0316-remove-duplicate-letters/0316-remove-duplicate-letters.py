class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
#         ord_set = sorted(set(s))
        
#         for i in ord_set:
#             index = s.index(i)
#             value = s[index:]
            
#             if len(set(value)) == len(ord_set):
#                 return i + self.removeDuplicateLetters(value.replace(i, ""))
        
#         return ''
        stack = []
        visited = set()
        
        last_occur = {}
        for i, letter in enumerate(s):
            last_occur[letter] = i
        
        for i, letter in enumerate(s):
            if letter not in visited:
                while stack and letter < stack[-1] and i < last_occur[stack[-1]]:
                    visited.remove(stack.pop())
                    
                stack.append(letter)
                visited.add(letter)
        
        return "".join(stack)
            