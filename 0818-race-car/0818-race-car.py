class Solution:
    def racecar(self, target: int) -> int:
        path = {(0, 1): None}
        queue = deque([(0, 1)])
        
        while queue:
            position, speed = queue.popleft()
            
            if position == target:
                current = (position, speed)
                break
            
            # choice-1 - acclerate
            new_pos = position + speed
            new_sp = speed * 2
            
            if (new_pos, new_sp) not in path:
                queue.append((new_pos, new_sp))
                path[(new_pos, new_sp)] = (position, speed)
            
            # choice-2 - reverse
            new_sp = -1 if speed > 0 else 1
            
            if (position, new_sp) not in path:
                queue.append((position, new_sp))
                path[(position, new_sp)] = (position, speed)
        
        count = -1
        while current:
            count += 1
            current = path[(current[0], current[1])]
        
        return count
            