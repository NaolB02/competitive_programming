class Solution:
    def interpret(self, command: str) -> str:
        interpreted = ''
        iterator = 0
        a= 1
        
        while iterator < len(command):
            if command[iterator] == "G":
                interpreted += "G"
                iterator += 1
            
            elif iterator + 1 < len(command) and command[iterator: iterator + 2] == "()":
                interpreted += "o"
                iterator += 2
            
            else:
                interpreted += "al"
                iterator += 4
        
        return interpreted