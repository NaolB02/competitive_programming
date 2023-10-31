class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        xor = 0
        
        for i in range(1, len(pref)):
            xor ^= arr[-1]
            arr.append(xor ^ pref[i])
        
        return arr