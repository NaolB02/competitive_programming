class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashcounter = Counter(nums)
        mincount = float('inf')
        numslist = []
        
        for num in hashcounter:
            numslist.append([num,hashcounter[num]])
        
        numslist.sort(reverse = True, key = lambda x: x[1])
        out = []
        
        for i in range(k):
            out.append(numslist[i][0])
        
        return out
            