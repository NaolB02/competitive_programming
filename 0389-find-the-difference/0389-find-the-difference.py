class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == '':
            return t[0]
        
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        
        return t[i + 1]