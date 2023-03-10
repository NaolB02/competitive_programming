class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)
        time = 0
        
        while tickets and tickets[k]:
            k -= 1
            
            if k == -1:
                k = len(tickets) - 1
                
            val = tickets.popleft()
            val -= 1
            tickets.append(val)
            
            if val >= 0:
                time += 1
                
            if tickets[k] == 0:
                return time
            
        return 0