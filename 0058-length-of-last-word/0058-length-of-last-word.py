class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        for var in range(len(s) - 1, -1 , -1):
            
            if s[var] != " ":
                i = var
                break
        
        j = i
        counter = 0
        while j >=0 and s[j] != " ":
            counter = counter + 1
            j = j - 1
        
        return counter
        