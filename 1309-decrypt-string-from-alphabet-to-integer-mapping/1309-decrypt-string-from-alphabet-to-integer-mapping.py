class Solution:
    def freqAlphabets(self, s: str) -> str:
        iterator = 0
        decrypted = ''
        
        while iterator < len(s):
            if iterator + 2 < len(s) and s[iterator + 2] == "#":
                encNum = int(s[iterator: iterator + 2])
                iterator += 3
                
            else:
                encNum = int(s[iterator])
                iterator += 1
            
            decrypted += chr(encNum + 96)
            
        return decrypted