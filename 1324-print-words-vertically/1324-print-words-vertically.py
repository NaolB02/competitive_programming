class Solution:
    def printVertically(self, s: str) -> List[str]:
        wordsList = s.split()
        verticallyPrinted = []
        # the length of the longest word from wordsList
        maxLength = len(max(wordsList, key = lambda x : len(x)))
        
        # iterates through each column of word
        for index in range(maxLength):
            verticalWord = []
            
            for ind in range(len(wordsList)):
                if len(wordsList[ind]) <= index:
                    verticalWord.append(' ')
                
                else:
                    verticalWord.append(wordsList[ind][index])
            
            # removes the trailing spaces
            for ind in range(len(verticalWord) - 1, -1, -1):
                if verticalWord[ind] == ' ':
                    verticalWord.pop()
                else:
                    break
            
            verticallyPrinted.append(''.join(verticalWord))
        
        return verticallyPrinted