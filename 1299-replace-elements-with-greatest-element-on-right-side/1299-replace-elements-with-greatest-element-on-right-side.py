
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        ans = [0] * len(arr)

        val = -1
        max_val  = -1
        for i in range(len(arr)-1, -1, -1):
            right_val = max_val
            max_val = max(arr[i], right_val )
            ans[i] =  right_val

        return ans 

