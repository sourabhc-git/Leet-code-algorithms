class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        set_ = set()
        max_len = 0
        j = 0
        i=0
        while(i<len(s)):
            if s[i] not in set_ :
                set_.add(s[i])
                max_len = max(i-j+1, max_len)
                i = i+1
            else:
                set_.remove(s[j])
                j += 1
        return max_len
                
                