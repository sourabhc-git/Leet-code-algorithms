# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def checkSubtree(root, subRoot):

            if not root and not subRoot:
                return True

            if root and subRoot and root.val == subRoot.val:
                return checkSubtree(root.left, subRoot.left) and checkSubtree(root.right, subRoot.right)            

            return False


        def checkRoot(root):
            
            if root is None:
                return False
            
            if checkSubtree(root, subRoot):
                return True
            
            return checkRoot(root.left) or checkRoot(root.right)

        return checkRoot(root)