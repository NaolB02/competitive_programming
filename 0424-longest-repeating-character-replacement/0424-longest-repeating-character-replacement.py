class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slidin_win = defaultdict(int)
        cur_max = 0
        max_length = 0
        left = 0
        
        for right, letter in enumerate(s):
            slidin_win[letter] += 1
            cur_max = max(cur_max, slidin_win[letter])
            count = right - left + 1
            
            if count - cur_max > k:
                slidin_win[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
    
        return max_length
        