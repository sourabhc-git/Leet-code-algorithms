class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        min_len_string = strs[0]
        
        for string in strs[1:]:
            
            if len(string) < len(min_len_string):
                
                min_len_string = string
        
        for index in range(0, len(min_len_string)):
            
            for new_string in strs:
                
                if new_string[index] != min_len_string[index]:
                    
                    return min_len_string[:index]
        
        
        return min_len_string
        