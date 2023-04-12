class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < (-2)**31:
            n = (-2)**31
        elif n > (2**31) - 1:
            n = (2**31) - 1
            
        if n == 0:
            return 1
        elif n < 0:
            return (1/x) * self.myPow(x, n+1)
        elif n > 0:
            return x * self.myPow(x, n-1)
        
    def easy(self, x, n):
        return x**n
        

print(Solution().myPow(5, -2))
