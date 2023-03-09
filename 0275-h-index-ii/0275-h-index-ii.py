class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low, high = 0, len(citations)
        
        while low <= high:
            mid = (high + low) // 2
            place = bisect_left(citations, mid)
            
            if len(citations) - place < mid:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return low - 1