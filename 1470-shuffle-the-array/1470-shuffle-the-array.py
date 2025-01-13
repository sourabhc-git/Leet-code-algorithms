class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        

        newIndex = n
        res = []
        start = 0
        while newIndex < 2 * n:

            res.append(nums[start])
            res.append(nums[newIndex])
            start = start + 1
            newIndex = newIndex + 1
        
        return res