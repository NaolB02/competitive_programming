class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        Area = 0

        while start < end:
            curHeight = min(height[start], height[end])
            curWidth = end - start
            curArea = curHeight * curWidth
            Area = max(Area, curArea)

            if height[start] >= height[end]: end -= 1
            
            else: start += 1


        return Area 