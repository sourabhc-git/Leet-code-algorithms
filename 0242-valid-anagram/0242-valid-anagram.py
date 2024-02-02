class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        list_1 = list(s)
        list_2 = list(t)
        
        if sorted(list_1) == sorted(list_2):
            return True
        else:
            return False
        

        

        