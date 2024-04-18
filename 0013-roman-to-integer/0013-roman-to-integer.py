class Solution:
    def romanToInt(self, s: str) -> int:
        
        dict1 = { "I" : 1 , "X" : 10, "V" : 5, "L" : 50, "C" : 100, "D" : 500, "M": 1000,
                  "IV": 4, "IX" : 9, "XL": 40, "XC": 90, "CD" : 400, "CM": 900}
        
        value = 0
        
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in dict1:
                value += dict1[s[i:i+2]]
                i += 2  # Move by 2 since we've consumed two characters
            elif s[i] in dict1:
                value += dict1[s[i]]
                i += 1
            else:
                return 0
        
        return value