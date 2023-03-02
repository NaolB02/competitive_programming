class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        levels = path.split("/")
        
        for level in levels:
            if level == ".." and stack:
                stack.pop()
            
            elif level == "." or not level or level == "..":
                pass
            
            else:
                stack.append(level)
        
        simplifiedPath = "/".join(stack)
        return "/" + simplifiedPath