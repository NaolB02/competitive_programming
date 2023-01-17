class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        
        for start in range(len(heights) - 1):
            min_index = start
            
            for index in range(start, len(heights)):
                if heights[index] > heights[min_index]:
                    min_index = index
            
            names[start], names[min_index] = names[min_index], names[start]
            heights[start], heights[min_index] = heights[min_index], heights[start]
        
        return names