class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        man_distance = float('inf')
        min_index = -1
        
        for index, point in enumerate(points):
            a = point[0]
            b = point[1]
            
            # checks if the current point is valid
            if a == x or b == y:
                cur_distance = abs(a - x) + abs(b - y)
                
                if cur_distance < man_distance:
                    min_index = index
                    man_distance = cur_distance
        
        return min_index