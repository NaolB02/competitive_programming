class Solution:
    def compress(self, chars: List[str]) -> int:
        start, end = 0, 1
        count = 1

        while end < len(chars):
            if chars[start] == chars[end]:
                count += 1
                chars.pop(end)
                
                if end >= len(chars):
                    if count > 9:
                        count = str(count)
                        
                        for i in range(len(count)):
                            chars.insert(end, count[i])
                            end += 1
                    else: 
                        chars.insert(end, str(count))
                        
                    break
            
            else:
                if count > 9:
                    count = str(count)
                    for i in range(len(count)):
                        chars.insert(end, count[i])
                        end += 1
                        
                elif count == 1:
                    pass
                    
                else: 
                    chars.insert(end, str(count))
                    end  += 1
                    
                start = end
                end += 1
                count = 1
        
        return len(chars)
            
            