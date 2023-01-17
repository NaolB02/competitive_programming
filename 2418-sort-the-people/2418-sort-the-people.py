class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        for index in range(size):
            swap = True
            for index2 in range(1, size):
                if heights[index2] > heights[index2 - 1]:
                    heights[index2], heights[index2 - 1] = heights[index2 - 1], heights[index2]
                    names[index2], names[index2 - 1] = names[index2 - 1], names[index2]
                    swap = False
                
            if swap:
                    break
        
        return names