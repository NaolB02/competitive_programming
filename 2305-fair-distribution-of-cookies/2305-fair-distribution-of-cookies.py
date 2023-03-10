class Solution:
    min_unfairness = math.inf
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        unfairness = []
        
        def backtrack(index):
            if index == len(cookies):
                self.min_unfairness = min(max(bucket), self.min_unfairness)
                return
            
            if self.min_unfairness < max(bucket):
                return
            
            if bucket.count(0) > len(cookies) - index:
                return
            
            for i in range(k):
                bucket[i] +=  cookies[index]
                backtrack(index + 1)
                bucket[i] -= cookies[index]
        
        
        backtrack(0)
        return self.min_unfairness