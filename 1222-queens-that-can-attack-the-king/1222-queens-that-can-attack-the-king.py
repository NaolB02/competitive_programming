class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        kx, ky = king[0], king[1]
        
        def calculate_distance(x, y):
            nonlocal ky
            nonlocal kx
            
            return (ky - y) ** 2 + (kx - x) ** 2
        
        positions = {'up': [kx + 100, ky + 100], 'down': [kx + 100, ky + 100], 'right': [kx + 100, ky + 100], 'left':[kx + 100, ky + 100], 'up-left': [kx + 100, ky + 100], 'up-right': [kx + 100, ky + 100], 'down-left': [kx + 100, ky + 100], 'down-right': [kx + 100, ky + 100]}
        new_nums = []
        
        for x, y in queens:
            cur_dist = calculate_distance(x, y)
            # check if the queen and king are in the same row
            if x == kx:
                if y > ky:
                    cx, cy = positions['right']
                    prev_dist = calculate_distance(cx, cy)
                    
                    if cur_dist < prev_dist: positions['right'] = [x, y]
                else:
                    cx, cy = positions['left']
                    prev_dist = calculate_distance(cx, cy)
                    
                    if cur_dist < prev_dist: positions['left'] = [x, y]
            
            # check if the queen and king are in the same column
            elif y == ky:
                if x > kx:
                    cx, cy = positions['up']
                    prev_dist = calculate_distance(cx, cy)
                    
                    if cur_dist < prev_dist: positions['up'] = [x, y]
                else:
                    cx, cy = positions['down']
                    prev_dist = calculate_distance(cx, cy)
                    
                    if cur_dist < prev_dist: positions['down'] = [x, y]
                    
            # check if the queen and king are in the same left-right diagonal
            elif x - y == kx - ky:
                if x > kx:
                    cx, cy = positions['down-right']
                    prev_dist = calculate_distance(cx, cy)
                    
                    if cur_dist < prev_dist: positions['down-right'] = [x, y]
                else:
                    cx, cy = positions['up-left']
                    prev_dist = calculate_distance(cx, cy)
                    
                    if cur_dist < prev_dist: positions['up-left'] = [x, y]
            
            # check if the queen and king are in the same right-left diagonal
            elif x + y == kx + ky:
                if y > ky:
                    cx, cy = positions['up-right']
                    prev_dist = calculate_distance(cx, cy)
                    
                    if cur_dist < prev_dist: positions['up-right'] = [x, y]
                else:
                    cx, cy = positions['down-left']
                    prev_dist = calculate_distance(cx, cy)
                    
                    if cur_dist < prev_dist: positions['down-left'] = [x, y]
        
        for x, y in positions.values():
            if x < 8 and y < 8:
                new_nums.append([x, y])
        
        return new_nums