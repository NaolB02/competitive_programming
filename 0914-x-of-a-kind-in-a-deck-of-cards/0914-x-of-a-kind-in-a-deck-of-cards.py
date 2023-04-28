class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck = Counter(deck)
        
        gcd = None
        for val in deck.values():
            if not gcd:
                gcd = val
                
            gcd = self.findGCD(val, gcd)
            
            if gcd == 1:
                return False
        
        return True
    
    def findGCD(self, a, b):
        if b == 0:
            return a
        
        return self.findGCD(b, a % b)