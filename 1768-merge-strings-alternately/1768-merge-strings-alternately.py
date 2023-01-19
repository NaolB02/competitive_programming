class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_temp = []

        for i in range(len(word1)):
            if i in range(len(word2)):
                word_temp.append(word1[i])
                word_temp.append(word2[i])
            elif i:
                word_temp.append(word1[i])

        if len(word1) < len(word2):
            word_temp.append(word2[len(word1):])         

        return ''.join(word_temp)