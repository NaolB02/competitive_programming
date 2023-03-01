class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        basket = {}
        maxFruits = 0

        while r < len(fruits):
            basket[fruits[r]] = r

            if len(basket) > 2:
                minIndex = min(basket.values())
                del basket[fruits[minIndex]]
                l = minIndex + 1
            
            maxFruits = max(maxFruits, r - l + 1)            
            r += 1
        
        return maxFruits

