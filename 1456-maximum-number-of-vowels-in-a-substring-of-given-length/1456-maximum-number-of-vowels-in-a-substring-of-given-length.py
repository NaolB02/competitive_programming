class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','i','o','u'])
        l = 0
        curCount = 0
        maxCount = 0

        for r in range(len(s)):
            if s[r] in vowels:
                curCount += 1
            
            if r - l >= k:
                if s[l] in vowels:
                    curCount -= 1
                l += 1

            maxCount = max(maxCount, curCount)

        return maxCount
            