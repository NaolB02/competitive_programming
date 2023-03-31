class Solution:
    def countBits(self, n: int) -> List[int]:
        one_count = []
        for i in range(n + 1):
            count = 0
            j = 1
            
            while j <= i:
                if j & i:
                    count += 1
                j <<= 1
            
            one_count.append(count)
        
        return one_count