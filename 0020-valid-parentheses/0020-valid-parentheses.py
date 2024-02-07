class Solution:
    def isValid(self, s: str) -> bool:
        
#         stack = []
        
#         dict_sign = {'(' : ')', '{': '}', '[': ']'}
        
#         if s == "":
#             return True
#         for char in s :
            
#             if char in dict_sign.keys():
#                 stack.append(char)
            
#             if char in dict_sign.values():
                
#                 if stack == [] or dict_sign[char] != stack.pop():
#                     return False
        
#         return stack == []
        
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
            
            