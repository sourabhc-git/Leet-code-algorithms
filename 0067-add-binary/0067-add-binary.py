class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        final_list = []
        
        carry = 0
        total = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry:
            
            total = carry
            
            if i>= 0:
                total = int(a[i]) + total
                i = i - 1
            
            if j >=0:
                total = int(b[j]) + total
                j = j - 1
                
            value = total % 2
            carry = total // 2
            
            final_list.append(str(value))
        
        rev_list = reversed(final_list)
        
        return ''.join(rev_list)
        