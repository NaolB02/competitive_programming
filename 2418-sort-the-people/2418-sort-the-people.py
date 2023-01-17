class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(names)
        
        freq = [[] for _ in range(max(heights) + 1)]
        
        for index, height in enumerate(heights):
            freq[height].append(names[index])
        
        names = []
        
        for lis in freq:
            for name in lis:
                names.append(name)
        
        return reversed(names)
        
        