class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        var_length = len(needle)
        
        pos = 0
        if needle in haystack:
            
            for i in range(0, len(haystack)):
                if haystack[i]  == needle[0]:
                    if haystack[i : (i + var_length)] == needle:
                        return i
        else:
            return -1
                        
        