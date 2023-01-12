class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        firstWord = [0] * 26
        offset = ord('a')
        
        for letter in words[0]:
            asci = ord(letter)
            firstWord[asci - offset] += 1
        
        for word in words:
            if word == words[0]:
                continue
            
            curWord = [0] * 26
            for letter in word:
                asci = ord(letter)
                curWord[asci - offset] += 1
                
            for index in range(len(firstWord)):
                firstWord[index] = min(firstWord[index], curWord[index])
        
        common = []
        for index, freq in enumerate(firstWord):
            for _ in range(freq):
                letter = chr(index + offset)
                common.append(letter)
        
        return common