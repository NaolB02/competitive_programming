class Solution:
    def countArrangement(self, n: int) -> int:
        visited = set()
        count = 0
        arr = []
        
        def backtrack(i):
            nonlocal n
            nonlocal count            
            
            if i == n + 1:
                count += 1
                return
            
            
            for j in range(1, n + 1):
                if j not in visited:
                    visited.add(j)
                    arr.append(j)
                    
                    if i % arr[i - 1] != 0 and arr[i - 1] % i != 0:
                        arr.pop()
                        visited.remove(j)
                        continue

                    backtrack(i + 1)

                    arr.pop()
                    visited.remove(j)
            
        backtrack(1)
        return count