class Solution:
    def maxLength(self, arr: List[str]) -> int:
        counter = [0]*26
        ans = 0
        
        def dfs(idx, cnt):
            nonlocal ans
            for i in range(26):
                if counter[i] > 1:
                    return
            
            if idx == len(arr):
                ans = max(ans, cnt)
                return
                
            # choose logic
            for char in arr[idx]:
                counter[ord(char) - 97] += 1
            
            dfs(idx + 1, cnt + len(arr[idx]))
            
            for char in arr[idx]:
                counter[ord(char) -97] -= 1
            
            # not choose logic
            
            dfs(idx + 1, cnt)
        
        dfs(0, 0)
        return ans
            