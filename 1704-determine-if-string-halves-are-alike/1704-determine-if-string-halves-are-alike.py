class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelset = set(vowels)
        halfnum = int(len(s) / 2)
        s1, s2 = s[0:halfnum], s[halfnum:]
        count1, count2 = 0, 0
        
        for i in range(halfnum):
            if s1[i] in vowelset:
                count1 += 1
            if s2[i] in vowelset:
                count2 += 1
        
        if count1 == count2:
            return True