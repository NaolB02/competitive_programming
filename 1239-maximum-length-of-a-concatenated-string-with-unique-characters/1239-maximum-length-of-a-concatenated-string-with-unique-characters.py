class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        def dfs(ind, arr, path):
            nonlocal res
            if len(set("".join(path))) == len("".join(path)):
                res = max(res, len("".join(path)))
                
            for i in range(ind + 1, len(arr)):
                if len(set(arr[i])) == len(arr[i]):
                    path.append(arr[i])
                    dfs(i, arr, path)
                    path.pop()
                    
        dfs(-1, arr, [])
        return res
                    
        
#         def check_unity(di):
#             for key in di:
#                 if di[key] > 1:
#                     return False
#             return True
        
#         max_sub = 0
#         n = len(arr)
#         let_dict = defaultdict(int)
        
#         def backtrack(i, string):
#             nonlocal max_sub
            
#             if len(let_dict) == len(string):
#                 max_sub = max(len(let_dict), max_sub)
            
#             else:
#                 return
            
#             if i == n:
#                 return
            
#             # case - 1
#             word = arr[i]
            
#             for letter in word:
#                 let_dict[letter] += 1
            
#             temp = string
#             string += word

#             backtrack(i + 1, string)
            
#             string = temp

#             for letter in word:
#                 let_dict[letter] -= 1
                
#                 if let_dict[letter] <= 0:
#                     del let_dict[letter]
            
#             # case - 2
#             backtrack(i + 1, string)
            
#         backtrack(0, '')
#         return max_sub
