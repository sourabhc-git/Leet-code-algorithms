class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:


        ans = 2 * [0] * len(nums)

        for i in range(0, len(nums)):

            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        
        return ans
