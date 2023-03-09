class Solution:
    def splitString(self, s: str) -> bool:
        
#         def check_consc(arr, n):
#             if len(arr) <= 1 or len("".join(arr)) != n:
#                 return False
            
#             for i in range(1, len(arr)):
#                 if int(arr[i - 1]) - int(arr[i]) != 1:
#                     return False
            
#             return True
        
        def splitter(i, list1):
            print(list1)
            
            if len(list1) >= 2 and int(list1[-2]) - int(list1[-1]) != 1:
                return False
            
            elif len(list1) > 1 and len("".join(list1)) == len(s):
                return True
            
            for index in range(i, len(s)):
                list1.append(s[i:index + 1])
                
                cond = splitter(index + 1, list1)
                
                if cond:
                    return True
                list1.pop()
        
        return splitter(0, [])
        