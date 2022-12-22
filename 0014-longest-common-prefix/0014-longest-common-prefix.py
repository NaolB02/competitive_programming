class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        comPre = ''
        print(strs)
     
        for i in range(len(strs[0])):
            letter = strs[0][i]
            flag = True
            
            for j in range(1, len(strs)):
                
                if letter == strs[j][i]:
                    pass
                else:
                    flag = False
                    break
            if flag:
                comPre += letter
            else:
                break
                
        return comPre