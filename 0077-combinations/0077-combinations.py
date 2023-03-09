class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def comb(initial, lis, n, k):
            if len(lis) == k:
                combinations.append(lis[:])
                return
            
            if initial > n:
                return
            
            #case 1
            comb(initial + 1, lis, n, k)
            
            #case 2
            lis.append(initial)
            comb(initial + 1, lis, n, k)
            lis.pop()
        
        comb(1, [], n, k)
    
        return combinations