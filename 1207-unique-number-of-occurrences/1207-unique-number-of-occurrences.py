class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmp = Counter(arr)
        occr = []
        for value in hashmp.values():
            occr.append(value)
        
        temp = set(occr)
        if len(temp) == len(occr):
            return True
        return False