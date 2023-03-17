class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, img1 = num1.split('+')
        real2, img2 = num2.split('+')
        
        real = eval(real1 + '*' + real2) - eval(img1[:-1] + '*' + img2[:-1])
        img = eval(real1 + '*' + img2[:-1]) + eval(img1[:-1] + '*' + real2)
        
        return str(real) + '+' + str(img) + 'i'
        