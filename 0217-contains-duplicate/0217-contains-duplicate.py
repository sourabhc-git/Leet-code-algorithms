class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         _set = set(nums)

         if len(nums) != len(_set):
             return True
         else:
             return False