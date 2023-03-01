class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        Stack = [0]
        
        for paren in s:
            if paren == "(":
                Stack.append(0)
            
            elif paren == ")":
                popped = Stack.pop()
                Stack[-1] += max(2 * popped, 1)
        
        return Stack[-1]