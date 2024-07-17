class Solution:
    
    
    def robber(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        new = []
        
        new.append(nums[0])
        new.append(max(nums[0], nums[1]))
        
        for i in  range(2, len(nums)):
            new.append(max(new[i-1], new[i-2]+ nums[i]))
        
        
        return new[-1]
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        
        value1 = self.robber(nums[:-1])
        value2 = self.robber(nums[1:])
        
        return max(value1, value2)
    
        