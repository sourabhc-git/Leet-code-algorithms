class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        dict_sign = {'(' : ')', '{': '}', '[': ']'}
        
        print(dict_sign.values())
        if s == "":
            return True
        for char in s :
            
            if char in dict_sign.keys():
                stack.append(char)
            
            elif char in dict_sign.values():
                
                if stack == [] or dict_sign[stack.pop()] != char :
                    return False
        
        return stack == []