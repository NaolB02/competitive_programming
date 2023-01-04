class Solution:
    def printVertically(self, s: str) -> List[str]:
        wordsList = s.split()
        verticallyPrinted = []
        maxLength = len(max(wordsList, key = lambda x : len(x)))
        
        for index in range(maxLength):
            verticalWord = []
            
            for ind in range(len(wordsList)):
                if len(wordsList[ind]) <= index:
                    verticalWord.append(' ')
                
                else:
                    verticalWord.append(wordsList[ind][index])
            
            for ind in range(len(verticalWord) - 1, -1, -1):
                if verticalWord[ind] == ' ':
                    verticalWord.pop()
                else:
                    break
            
            verticallyPrinted.append(''.join(verticalWord))
        
        return verticallyPrinted