class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            mid = low + (high - low) // 2
            
            curDays = 0
            summ = 0
            for index in range(len(weights)):
                summ += weights[index]
                
                if summ > mid:
                    curDays += 1
                    summ =  weights[index]
                    
            curDays += 1
            
            if curDays <= days:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return low