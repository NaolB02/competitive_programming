class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curPeople = 0
        minFrom = float('inf')
        maxTo = 0
        
        for i in range(len(trips)):
            if trips[i][1] < minFrom:
                minFrom = trips[i][1]
            if trips[i][2] > maxTo:
                maxTo = trips[i][2]
        
        trips.sort(key = lambda x: x[1])
        
        
        for i in range(minFrom, maxTo + 1):
            for j in range(len(trips)):
                if i == trips[j][1]:
                    curPeople += trips[j][0]
                if i == trips[j][2]:
                    curPeople -= trips[j][0]
                
                if curPeople > capacity:
                    print(i, j)
                    return False
        return True