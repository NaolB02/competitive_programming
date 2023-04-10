class Solution:
    def minWindow(self, s: str, t: str) -> str:
        another_t = t
        summ = len(t)
        t = Counter(t)
        another_t = Counter(another_t)
        l, min_win = 0, [-math.inf, math.inf]

        for r in range(len(s)):
            if s[r] in t and t[s[r]] > 0:
                summ -= 1
                t[s[r]] -= 1
            
            elif s[r] in t:
                t[s[r]] -= 1
                        
            while summ == 0:
                if min_win[1] - min_win[0] + 1 > r - l + 1:
                    min_win[0], min_win[1] = l, r

                if s[l] in t and 0 <= t[s[l]] < another_t[s[l]]:
                    summ += 1
                    t[s[l]] += 1
                
                elif s[l] in t:
                    t[s[l]] += 1

                l += 1
        
        try:
            return s[min_win[0]: min_win[1] + 1]
        
        except:
            return ''