# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        def goodFunction(nodevalue, val):
            
            if not nodevalue:
                return
            
            if nodevalue.val >= val:
                self.count = self.count + 1

            value = max(nodevalue.val, val)
            goodFunction(nodevalue.left, value)
            goodFunction(nodevalue.right, value)
        

        goodFunction(root, root.val)
        return self.count