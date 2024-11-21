class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total = sum(nums)
        n = len(nums)
        new_total = n * ((n + 1) / 2)
        
        return int(new_total - total)