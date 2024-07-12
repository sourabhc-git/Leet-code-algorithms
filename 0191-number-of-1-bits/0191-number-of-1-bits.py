from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        
        binary_num = bin(n)[2:]
        
        list_val = list(str(binary_num))
        
        
        val = Counter(list_val)['1']

        return val