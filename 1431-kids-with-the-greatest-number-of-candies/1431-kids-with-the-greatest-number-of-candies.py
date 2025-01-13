class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        res = [False] * len(candies)
        for i in range(0, len(candies)):

            newcandy = candies[i] + extraCandies

            if newcandy >= max(candies):
                res[i] = True

        return res