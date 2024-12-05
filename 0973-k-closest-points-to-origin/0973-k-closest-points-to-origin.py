import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist_heap = []
        
        
        for i in points:
            
            value = math.sqrt(i[0]*i[0] + i[1]*i[1])
            heapq.heappush(dist_heap, (value, i))
        
        final = []
        for _ in range(0, k):
            final.append(heappop(dist_heap)[1])
            
        
        return final