class Solution:
    def removeStars(self, s: str) -> str:
        editedStr = []
        
        for letter in s:
            if letter == "*":
                editedStr.pop()
            
            else:
                editedStr.append(letter)
                
        
        return "".join(editedStr)