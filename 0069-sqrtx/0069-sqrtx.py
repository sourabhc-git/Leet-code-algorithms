class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        for num in range(x // 2 + 1):
            if num * num == x:
                return num
            elif num * num > x:
                return num - 1
        
        return x // 2
        