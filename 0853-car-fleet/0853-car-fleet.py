class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ordered = [[position[index], speed[index]] for index in range(len(position))]
        ordered.sort(key = lambda x: x[0])
        remaining = []
        
        for pos, sp in ordered:
            remaining.append((target - pos) / sp)
                
        for index in range(len(remaining) - 1, -1, -1):
            if index - 1 == -1:
                break
                
            if remaining[index] > remaining[index - 1]:
                remaining[index - 1] = remaining[index]
            
                
        return len(set(remaining))