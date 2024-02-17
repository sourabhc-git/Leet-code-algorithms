class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        for i in range(1, len(nums)):
             prefix.append(prefix[i - 1] * nums[i - 1])


        product = 1
        suffix  = []
        for num in reversed(nums):
            suffix.append(product)
            product *= num

        suffix = list(reversed(suffix))

        ans = []

        for i in range(0, len(nums)):
            ans.append(prefix[i] * suffix[i])

        return ans