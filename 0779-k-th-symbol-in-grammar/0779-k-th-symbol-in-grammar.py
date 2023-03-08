class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        new_k = (k + 1) // 2
        prev = self.kthGrammar(n - 1, new_k)

        if k % 2:
            return prev

        return 1 - prev