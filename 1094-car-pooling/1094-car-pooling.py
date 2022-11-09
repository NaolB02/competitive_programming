class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curPeople = 0      
        loc = {}
        
        
        
        for people, start, end in trips:
            loc[start] =loc.get(start,0)+ people
            loc[end] =loc.get(end,0)- people
        
        for i in sorted(loc):
            curPeople += loc[i]
            if curPeople > capacity:
                return False
        return True