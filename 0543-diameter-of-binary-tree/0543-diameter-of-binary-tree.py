# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

            length = float("-inf")
            def findDiameter(root):
                nonlocal length

                if not root:
                    return 0

                left = findDiameter(root.left)
                right = findDiameter(root.right)
            
                ans = 1 + max(left, right)
                length = max(length, left + right)
                return ans

            findDiameter(root)
            return length