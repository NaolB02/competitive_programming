class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_req = 0
        buildings = [0] * n
        count = 0
        count2 = 0
        
        def check_zero(lis):
            
            for el in lis:
                if el != 0:
                    return False
            return True
        
        def backtrack(i):
            nonlocal max_req
            nonlocal count
            
            if check_zero(buildings):
                max_req = max(max_req, count)
            
            if i == len(requests):
                return
            
            # case - 1
            buil_from = requests[i][0]
            buil_to = requests[i][1]

            buildings[buil_from] -= 1
            buildings[buil_to] += 1

            count += 1

            backtrack(i + 1)

            count -= 1

            buildings[buil_from] += 1
            buildings[buil_to] -= 1

            # case - 2
            backtrack(i + 1)

        
        backtrack(0)
        return max_req