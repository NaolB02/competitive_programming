class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        else:
            new_k = (k + 1) // 2
            prev = self.kthGrammar(n - 1, new_k)
            
            if not prev:
                if k % 2:
                    return 0
                else:
                    return 1
            
            else:
                if k % 2:
                    return 1
                else:
                    return 0