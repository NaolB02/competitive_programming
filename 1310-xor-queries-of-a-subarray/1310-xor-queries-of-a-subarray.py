class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prexor = [arr[0]]
        out = []
        for i in range(1, len(arr)):
            prexor.append(prexor[i - 1] ^ arr[i])
        
        for j in range(len(queries)):
            left = queries[j][0]
            right = queries[j][1]
            if left == 0:   out.append(prexor[right])
            else:   out.append(prexor[right] ^ prexor[left - 1])
        
        return out