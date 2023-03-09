class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def get_comb(initial, list1, n, k):
            list1.append(initial)
            
            if len(list1) == k:
                combinations.append(list1)
                return
            
            for index in range(initial + 1, n + 1):
                get_comb(index,[num for num in list1], n, k)
        for index in range(1,n+1):
            get_comb(index,[],n,k)
        
        return combinations