class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spacedPhrase = []
        spacesIndex = 0
        
        for index, letter in enumerate(s):
            if spacesIndex < len(spaces):
                if index == spaces[spacesIndex]:
                    spacedPhrase.append(' ')
                    spacesIndex += 1
            
            spacedPhrase.append(letter)
        
        return ''.join(spacedPhrase)