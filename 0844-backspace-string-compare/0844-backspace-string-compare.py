class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        
        for letter in s:
            if stackS and letter == "#":
                stackS.pop()
            
            elif letter != "#":
                stackS.append(letter)
            
        
        for letter in t:
            if stackT and letter == "#":
                stackT.pop()
            
            elif letter != "#":
                stackT.append(letter)
        
        return stackS == stackT