class Solution:
    def turnLock(self, cur_state, i, direction):
        lock_rotated = int(cur_state[i])
        
        if direction == 1:
            if lock_rotated == 9:
                lock_rotated = 0
            else:
                lock_rotated += 1
        
        else:
            if lock_rotated == 0:
                lock_rotated = 9
            else:
                lock_rotated -= 1
        
        return str(lock_rotated)
    
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        deadends = set(deadends)
        queue = deque([start])
        path = {start: None}
        goal = None
        
        while queue:
            cur_state = queue.popleft()
            
            if cur_state == target:
                goal = cur_state
                break
            
            if cur_state in deadends:
                continue
            
            for i in range(4):
                # when rotated forward
                lock_rotated = self.turnLock(cur_state, i, 1)
                new_state = cur_state[0: i] + lock_rotated + cur_state[i + 1:]
                
                if new_state not in path:
                    queue.append(new_state)
                    path[new_state] = cur_state
                
                # when rotated backward
                lock_rotated = self.turnLock(cur_state, i, -1)
                new_state = cur_state[0: i] + lock_rotated + cur_state[i + 1:]
                
                if new_state not in path:
                    queue.append(new_state)
                    path[new_state] = cur_state
        
        count = -1
        while goal:
            count += 1
            goal = path[goal]
        
        return count