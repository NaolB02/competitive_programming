class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = Counter(s1)
        sldwin = {}
        l = 0
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            if s2[i] in s1count:
                sldwin[s2[i]] = sldwin.get(s2[i], 0) + 1
    
        for r in range(len(s1), len(s2)):
            if sldwin == s1count:
                return True

            if s2[r] in s1count:
                sldwin[s2[r]] = sldwin.get(s2[r], 0) + 1
            
            if s2[l] in sldwin:
                if sldwin[s2[l]] > 1:
                    sldwin[s2[l]] -= 1
                else:
                    del sldwin[s2[l]]
            l += 1

        if sldwin == s1count:
                return True