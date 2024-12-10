from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()

        result = []
        for i in range(0, len(nums)):

            if dq and dq[0] <= i-k:
                dq.popleft()
            
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            dq.append(i)
            if i >= k-1:
                result.append(nums[dq[0]])
        
        return result




            
                
            
            
            
            
            
        
        