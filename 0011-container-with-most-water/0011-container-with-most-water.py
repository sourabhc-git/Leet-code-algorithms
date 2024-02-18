import heapq
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #use two pointer solution
        
        i = 0
        
        j = len(height) - 1
        
        max_area = 0
        while i < j :
            
            height1 = min(height[i], height[j])
            
            area1 = height1 * (j - i)
            max_area = max(max_area, area1)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
        
        
            
                   
            
        
        