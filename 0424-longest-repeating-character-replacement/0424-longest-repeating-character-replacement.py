class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        
        max_num = 0
        
        count  = {}
        
        
        for i in range(0, len(s)):
            
            count[s[i]] = 1 + count.get(s[i], 0)  #here we can get the character count if its present or else 0
            
            max_num = max(max_num, count[s[i]])
            
            if (i - l + 1) - max_num > k :
                
                count[s[l]] -=1
                l +=1
            
        
        return (i - l + 1)



            
            
    
        