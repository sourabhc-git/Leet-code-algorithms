class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(0, len(matrix)):
            low = 0
            high = len(matrix[0])-1
            while low <= high:

                mid  = int((low + high)/2)
                print(matrix[i][mid])
                if matrix[i][mid] == target:
                    return True
                elif target > matrix[i][mid]:
                    low = mid + 1
                elif target < matrix[i][mid]:
                    high = mid - 1
                    
            
        return False