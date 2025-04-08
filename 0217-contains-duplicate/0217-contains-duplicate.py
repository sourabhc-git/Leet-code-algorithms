class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        new_set = set()


        for num in nums:

            if num not in new_set:
                new_set.add(num)
            else:
                return True
        
        return False
        