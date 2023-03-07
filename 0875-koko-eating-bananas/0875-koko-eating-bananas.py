class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)        
        low, high = 1, maxPile
        
        while low <= high:
            mid = low + (high - low) // 2
            
            cur_hours = 0
            for pile in piles:
                cur_hours += pile // mid
                
                if pile % mid:
                    cur_hours += 1
            
            if cur_hours <= h:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return low
        