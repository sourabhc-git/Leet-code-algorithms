class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Use dict.fromkeys to remove duplicates and maintain order
        unique_nums = list(dict.fromkeys(nums))

        # Modify the original list to reflect the unique elements
        nums[:len(unique_nums)] = unique_nums

        # Return the number of unique elements
        return len(unique_nums)
        