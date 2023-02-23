class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        asOrd=[ord(letter)-97 for letter in s]
        preSum=[0]*len(s)
        for shift in shifts:
            start,end,direction=shift
            if not direction:
                direction=-1
            preSum[start]+=direction
            if end!=len(s)-1:
                preSum[end+1]-=direction
        for index in range(1,len(preSum)):
            preSum[index]+=preSum[index-1]
        letters=[]
        for index,num in enumerate(preSum):
            letter=chr(((num+asOrd[index])%26)+97)
            letters.append(letter)
        return "".join(letters)