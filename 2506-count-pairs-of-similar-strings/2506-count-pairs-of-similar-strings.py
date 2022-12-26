class Solution:
    def similarPairs(self, words: List[str]) -> int:
        pairs = 0
        
        for index in range(len(words)):
            word = set(words[index])
            
            for index2 in range(index + 1, len(words)):
                if word == set(words[index2]):
                    pairs += 1
        
        return pairs