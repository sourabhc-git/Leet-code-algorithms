class Solution:
    def romanToInt(self, s: str) -> int:

        sum = 0
        i= 0
        
        dictionary = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M' : 1000}
        
        while i < len(s):
              
                if i + 1 < len(s) and dictionary[s[i+1]] > dictionary[s[i]] :
                    sum = sum + (dictionary[s[i+1]] - dictionary[s[i]])
                    i = i + 2
                else:
                    sum = sum + (dictionary[s[i]])
                    i = i + 1
        
        return sum
            
            
            