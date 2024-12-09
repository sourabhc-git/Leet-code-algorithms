class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_a = set(nums)

        max_length = 0
        for i in nums:

            if (i-1) not in set_a:
                length = 1
                next_num = i + 1

                while next_num in set_a:
                    length = length + 1
                    next_num = next_num + 1
                
                max_length = max(max_length, length)

        return max_length
                

        