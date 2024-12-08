class Solution:
    def isHappy(self, n: int) -> bool:


        seen = set()
        def check(n):

            while n!=1 and n not in seen:
                _sum = 0
                seen.add(n)
                for digit in str(n):
                    _sum = _sum + (int(digit)* int(digit))

                n = _sum
            return n==1
        if check(n):
            return True
        else:
            return False

