class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final_value = {}
        
        for word in strs:
            
            if tuple(sorted(word)) in  final_value:
                final_value[tuple(sorted(word))].append(word)
            else:
                final_value[tuple(sorted(word))] = [word]
        
        
        return list(final_value.values())
                
        
            
        
                    
                
            
            
            