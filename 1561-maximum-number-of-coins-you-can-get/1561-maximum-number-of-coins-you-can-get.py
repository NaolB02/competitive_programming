class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        out = 0
        i = 0
        
        while i < len(piles):
            alice = piles.pop()
            me = piles.pop()
            out += me
            i += 1
        
        return out