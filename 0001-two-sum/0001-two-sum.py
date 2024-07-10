class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        dictionary_1 = enumerate(nums)
        
        dictionary = {}
        for index, value in dictionary_1:
            
            if (target - value) in dictionary:
                
                return [dictionary[target-value], index]
            
            else:
                
                dictionary[value] = index
                
    
            
            

            
        