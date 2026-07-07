class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total=0
        x=""

        for digit in str(n):
            total+=int(digit)
            if digit!="0":
                x+=digit
        
        if x=="":
            return 0
        return int(x)*total