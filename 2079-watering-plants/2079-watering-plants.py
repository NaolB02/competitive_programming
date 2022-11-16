class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        totwat = 0
        tempcap = capacity
        i = 0

        while i < len(plants):
            
            if tempcap >= plants[i]:
                totwat += 1
                tempcap -= plants[i]
                i += 1
            
            else:
                totwat += 2 * i
                tempcap = capacity

        return totwat
