class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        merge = ''
        
        while word1 and word2:
            if word1 > word2:
                merge += word1.pop(0)
            
            else:
                merge += word2.pop(0)
        
        if word1:
            merge += ''.join(word1)
        
        if word2:
            merge += ''.join(word2)
        
        return merge