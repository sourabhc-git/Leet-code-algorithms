class Solution:
    def isValid(self, s: str) -> bool:
        
        hash_map = { '{': '}', '[' : ']', '(' : ')'}
        
        stack = []
        for i in s:
            if i in hash_map:
                stack.append(i)
            elif not stack or hash_map[stack.pop()] != i:
                return False
        
        return not stack
        
            
            
        
        
        