class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # joins the current integers into an address
        def join_int(arr):
            ans = []
            
            for lis in arr:
                ans.append(''.join(lis))
            
            return '.'.join(ans)
        
        addresses = []
        cur_add = [[] for i in range(4)]
        
        cur_add[0].append(s[0])
        
        def backtrack(i, container):
            # checking for leading zeros
            if len(cur_add[container]) > 1 and cur_add[container][0] == '0':
                return
            
            # checking if any number in the four integers is greater than 255
            if int(''.join(cur_add[container])) > 255:
                return
            
            # checking if the current built address is valid
            if i == len(s) and container == 3:
                addresses.append(join_int(cur_add))
                return
            
            elif i == len(s):
                return
            
            
            # choice 1 - current num is put in the same container as the previous one
            cur_add[container].append(s[i])
            backtrack(i + 1, container)
            cur_add[container].pop()
            
            # choice 2 - current num is put in the next container
            if container + 1 != 4:
                cur_add[container + 1].append(s[i])
                backtrack(i + 1, container + 1)
                cur_add[container + 1].pop()
            
            else:
                return
        
        backtrack(1, 0)
        return addresses