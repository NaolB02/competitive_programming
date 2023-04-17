class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        cur_max = max(candies)
        result = [False] * len(candies)
        
        for index, candy in enumerate(candies):
            if candy + extraCandies >= cur_max:
                result[index] = True
            
        return result