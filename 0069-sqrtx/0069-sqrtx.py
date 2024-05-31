class Solution:
    def mySqrt(self, x: int) -> int:
        
#         if x < 2:
#             return x
        
#         for num in range(x // 2 + 1):
#             if num * num == x:
#                 return num
#             elif num * num > x:
#                 return num - 1
        
#         return x // 2

        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            num = mid * mid
            
            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right