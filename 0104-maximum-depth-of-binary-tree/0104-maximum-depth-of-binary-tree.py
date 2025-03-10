# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

            def findDepth(root):
                nonlocal length

                if not root:
                    return 0

                left = findDepth(root.left)
                right = findDepth(root.right)
            
                ans = 1 + max(left, right)
                return ans

            return findDepth(root)