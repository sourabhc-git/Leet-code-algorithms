class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=nums[0]
        maxs=cur
        for i in range(1,len(nums)):
            cur=max(cur+nums[i],nums[i])
            maxs=max(maxs,cur)
            
        return maxs