class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        
        return result
if __name__=="__main__":
    pointer=Solution()
    x=pointer.myPow(2,9)
    print(x)