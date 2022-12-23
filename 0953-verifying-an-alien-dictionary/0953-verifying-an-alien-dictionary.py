class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        l, r = 0, 1
        
        while r < len(words):
            letter1 = words[l]
            letter2 = words[r]
            
            for i in range(min(len(letter1), len(letter2))):
                f1, f2 = letter1[i], letter2[i]
                index1, index2 = order.index(f1), order.index(f2)
                
                if index1 > index2:
                    return False
                
                elif index1 < index2:
                    break
                
                # handle edge case
                if i == len(letter2) - 1 and len(letter1) > len(letter2):
                    return False
            r += 1
            l += 1
            
        return True