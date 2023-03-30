class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ord_set = sorted(set(s))
        
        for i in ord_set:
            index = s.index(i)
            value = s[index:]
            
            if len(set(value)) == len(ord_set):
                return i + self.removeDuplicateLetters(value.replace(i, ""))
        
        return ''
            