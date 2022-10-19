# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node,lbound,rbound):
            if not node:
                return True
            if not (node.val < rbound and node.val > lbound):
                return False
            return isValid(node.left,lbound,node.val) and isValid(node.right,node.val,rbound)
        
        return isValid(root,-math.inf,math.inf)

