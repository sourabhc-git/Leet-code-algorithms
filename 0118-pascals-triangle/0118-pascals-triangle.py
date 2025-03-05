class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans_list = [[1]]

        for i in range(1, numRows):
            new_list = [1]
            for j in range(1, len(ans_list[i-1])):
                new_list.append(ans_list[i-1][j] + ans_list[i-1][j-1])
            new_list.append(1)
            ans_list.append(new_list)
        

        return ans_list


            
