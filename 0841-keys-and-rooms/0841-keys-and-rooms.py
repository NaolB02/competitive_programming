class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        presence = [0] * len(rooms)
        presence[0] = 1
        queue = deque(rooms[0])
        
        while queue:
            current = queue.popleft()
            presence[current] = 1
            
            for room in rooms[current]:
                if not presence[room] and room not in queue:
                    queue.append(room)
        
        for p in presence:
            if not p:
                return False
        
        return True