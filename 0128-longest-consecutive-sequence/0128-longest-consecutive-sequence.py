class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        
        sorted_list = sorted(nums)
        
        hash_map = {}
        count = 1
        new_list = [sorted_list[0]]
        for i in range(1, len(sorted_list)):
            
            if (sorted_list[i] - sorted_list[i - 1] ) ==  1 :
                count = count + 1
                new_list.append(sorted_list[i])
            elif sorted_list[i] == sorted_list[i - 1]:
                # Handle duplicate elements
                continue
            else:
                hash_map[count] = new_list
                count = 1
                new_list = [sorted_list[i]]
                
        hash_map[count] = new_list
        
        return max(hash_map.keys())
                
                
                
        