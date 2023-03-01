class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def revString(s, p1 = 0, p2 = len(s) - 1):
            if p1 >= p2:
                pass
            else:
                s[p1], s[p2] = s[p2], s[p1]
                revString(s, p1 + 1, p2 - 1)
        
        revString(s, 0, len(s) - 1)