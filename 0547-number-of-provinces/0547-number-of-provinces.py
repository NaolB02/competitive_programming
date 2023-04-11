class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False for i in range(len(isConnected))]
        
        def inbound(row):
            return 0 <= row < len(isConnected)
        
        def dfs(row):
            visited[row] = True
            
            for i in range(len(isConnected[row])):
                if isConnected[row][i] and not visited[i] and row != i:
                    dfs(i)
            
            return
    
        count = 0
        for r in range(len(isConnected)):
            if not visited[r]:
                count += 1
                dfs(r)
        
        return count
        