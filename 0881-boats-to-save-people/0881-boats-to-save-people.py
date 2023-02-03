class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        start = 0
        end = len(people) - 1
        people.sort()

        while start <= end:
            
            if people[start] + people[end] <= limit:
                boats += 1
                start += 1
                end -= 1
            
            else:
                boats += 1
                end -= 1
        
        return boats