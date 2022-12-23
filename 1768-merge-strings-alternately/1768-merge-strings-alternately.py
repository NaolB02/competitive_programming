class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1, pointer2 = 0, 0
        merged = ''
        
        # even if one of the strings is iterated fully 
        # the other will continue to be iterated
        while pointer1 < len(word1) or pointer2 < len(word2):
            if pointer1 < len(word1):
                merged += word1[pointer1]
                pointer1 += 1
            
            if pointer2 < len(word2):
                merged += word2[pointer2]
                pointer2 += 1
            
        return merged
        