class Solution:
    def countBits(self, n: int) -> List[int]:


        new_list = []

        for i in range(0, n+1):
            count = 0
            while(i):

                if (i&1):
                    count = count + 1
                
                i = i>>1
            
            new_list.append(count)
        
        return new_list