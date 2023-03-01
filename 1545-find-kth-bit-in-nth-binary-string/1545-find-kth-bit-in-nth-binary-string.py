class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def findSn(n):
            if n == 1:
                return ["0"]
            
            else:
                sbefore = findSn(n - 1)
                ogs = sbefore.copy()
                for index in range(len(sbefore)):
                    if sbefore[index] == "0":
                        sbefore[index] = "1"
                    
                    else:
                        sbefore[index] = "0"
                    
                sbefore.reverse()
                return ogs + ["1"] + sbefore
        
        return findSn(n)[k - 1]