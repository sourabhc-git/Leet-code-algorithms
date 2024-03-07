class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        new_set = set()
        
        if (len(nums) <= 1):
            return False
        new_set.add(nums[0])
        for index in range(1, len(nums)):
            if nums[index] in new_set:
                return True
            else:
                new_set.add(nums[index])
        
        return False