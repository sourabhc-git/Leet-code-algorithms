class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        n1 = len(s1)

        n2 = len(s2)

        if n1 > n2:
            return False
        
        s1_values = [0] * 26
        s2_values = [0] * 26

        for  i in range(len(s1)):

            s1_values[ord(s1[i]) - 97] += 1
            s2_values[ord(s2[i]) - 97] +=1
        
        if s1_values == s2_values:
            return True
        
        for j in range(n1, n2):

            s2_values[ord(s2[j]) - 97] += 1
            s2_values[ord(s2[j -n1]) - 97] -=1

            if s1_values == s2_values:
                return True
        
        return False

            
            
            
            
        
        
            
        
            
        
            
                
            
        
        
            