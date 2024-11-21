class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1 = sorted(s1)
        
        
        left = 0
        right = len(s1)-1
        
        while (right != len(s2)):
            if "".join(s1) in "".join(sorted(s2[left:right+1])):
                return True
            
            left +=1
            right +=1
        
        return False
            
                
            
        
        
            