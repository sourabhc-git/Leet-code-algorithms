class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hash_map_s1 = {}
        hash_map_s2 = {}
        
        if len(s1) > len(s2):
            return False
        
        for i in range(0, len(s1)):
            hash_map_s1[s1[i]] = hash_map_s1.get(s1[i], 0) + 1
            hash_map_s2[s2[i]] = hash_map_s2.get(s2[i], 0) + 1
        
        if hash_map_s1 == hash_map_s2:
            return True
        
        for j in range(len(s1), len(s2)):
            
            start_element = (j - len(s1))
            end_element = j
            
            hash_map_s2[s2[start_element]] = hash_map_s2.get(s2[start_element], 0) - 1
            hash_map_s2[s2[end_element]] = hash_map_s2.get(s2[end_element], 0) +1
            
            if hash_map_s2[s2[start_element]] == 0:
                del hash_map_s2[s2[start_element]]
            
            if hash_map_s1 == hash_map_s2:
                return True
            
            
        return False
            
            
            
            
        
        
            
        
            
        
            
                
            
        
        
            