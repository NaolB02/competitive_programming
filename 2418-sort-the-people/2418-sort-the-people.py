class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        
        for index in range(1, size):
            for index2 in range(index - 1, -1 , -1):
                if heights[index] > heights[index2]:
                    heights[index], heights[index2] = heights[index2], heights[index]
                    names[index], names[index2] = names[index2], names[index]
                    index = index2
                
                else:
                    break
        
        return names