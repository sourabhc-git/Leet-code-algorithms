class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
              
            digit = ''.join(map(str, digits))
            
            int_digit = int(digit)
            
            incremental_value = int_digit + 1
            
            str_digit = str(incremental_value)
            
            digit_list = [int(value) for value in str_digit]
            
            return digit_list