class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1 = enumerate(nums)
        dict_2 = {}
        for keys, values in dict(dict_1).items():
            complement = target - values
            if complement in dict(dict_2).keys():
                return dict_2[complement], keys
            else:
                dict_2[values] = keys 
            
        