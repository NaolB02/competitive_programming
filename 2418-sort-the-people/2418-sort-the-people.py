class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        for index in range(size):
            for index2 in range(1, size):
                if heights[index2] > heights[index2 - 1]:
                    heights[index2], heights[index2 - 1] = heights[index2 - 1], heights[index2]
                    names[index2], names[index2 - 1] = names[index2 - 1], names[index2]
        
        return names