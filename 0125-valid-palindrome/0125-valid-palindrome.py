class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(filter(str.isalnum, s))
        new_s = new_s.lower()
        if new_s == "":
            return True
        start, end = 0, len(new_s) - 1

        while start < end:
            if new_s[start] == new_s[end]:
                start += 1
                end -= 1
            else:
                return False
                break
        
        return True
