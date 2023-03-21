class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def check_unity(di):
            for key in di:
                if di[key] > 1:
                    return False
            return True
        
        max_sub = 0
        n = len(arr)
        let_dict = defaultdict(int)
        
        def backtrack(i):
            nonlocal max_sub
            
            if check_unity(let_dict):
                max_sub = max(len(let_dict), max_sub)
            
            else:
                return
            
            if i == n:
                return
            
            # case - 1
            word = arr[i]
            
            for letter in word:
                let_dict[letter] += 1

            backtrack(i + 1)

            for letter in word:
                let_dict[letter] -= 1
                
                if let_dict[letter] <= 0:
                    del let_dict[letter]
            
            # case - 2
            backtrack(i + 1)
            
        backtrack(0)
        return max_sub
