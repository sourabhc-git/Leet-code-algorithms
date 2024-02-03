class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)):
            new = target - nums[i]
            try:
                second_index = nums.index(new, i+1, len(nums))
            except ValueError:
                continue
            
            return i, second_index