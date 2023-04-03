class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitwords = [0] * len(words)
        
        for i, word in enumerate(words):
            for letter in word:
                ord_let = ord(letter) - 97
                bitwords[i] |= (1 << ord_let)
        
        max_prod = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitwords[i] & bitwords[j] == 0:
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
        
        return max_prod
                
        