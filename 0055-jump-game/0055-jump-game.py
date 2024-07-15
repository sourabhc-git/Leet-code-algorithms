class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for j in range(goal -1,-1, -1 ):
            if (j + nums[j]) >=goal:
                goal = j
        
        if goal == 0:
            return True
        else:
            return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        