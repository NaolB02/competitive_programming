class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        out = []
        hashset = set()
        
        for r in range(len(s)):
            hashset.add(s[r])
            if r != len(s) - 1:
                count = 0
                for element in hashset:                    
                    if element in s[r + 1:]:
                        break
                    count += 1
    
                if count == len(hashset):
                    out.append(r - l + 1)
                    l = r + 1
                    hashset.clear()

        out.append(r - l + 1)
        return out
                