class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcounter = Counter(p)
        l = 0
        sldwin = {}
        out = []
        if len(s) < len(p):
            return []
        
        for i in range(len(p)):
            if s[i] in pcounter:
                sldwin[s[i]] = sldwin.get(s[i], 0) + 1
        
        for r in range(len(p), len(s)):
            if sldwin == pcounter:
                out.append(l)
            
            if s[r] in pcounter:
                sldwin[s[r]] = sldwin.get(s[r], 0) + 1
            
            if s[l] in sldwin and sldwin[s[l]] > 1:
                sldwin[s[l]] -= 1
            elif s[l] in sldwin:
                del sldwin[s[l]]
            l += 1
        
        if sldwin == pcounter:
            out.append(l)
        return out
                
                