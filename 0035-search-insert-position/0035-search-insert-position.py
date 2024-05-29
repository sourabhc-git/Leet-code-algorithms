class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i = 0
        j = len(nums) - 1
        
        if target > nums[j]:
            return (j + 1)
        
        if target < nums[0]:
            return 0 
        while(1):
            
            if nums[i] < target:
                i = i + 1
            if nums[j] > target:
                j = j - 1
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if nums[j] < target < nums[i]:
                return i
            
            
        