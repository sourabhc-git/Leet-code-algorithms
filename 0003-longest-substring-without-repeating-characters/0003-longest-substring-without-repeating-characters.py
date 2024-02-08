class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = []
        length = 0
        new_length = 0
        for i in range(0, len(s)):
            
            for j in range(i, len(s)):
                if s[j] not in visited:
                    visited.append(s[j])
                else:
                    new_length = len(visited)
                    length = max(length, new_length)
                    visited = []
                    break
        if len(s) == 1:
            return 1
        
        return length
            
        