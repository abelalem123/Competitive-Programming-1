# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if not root or root.val>targetSum:
        #     return False
        def search(i,node):
            if not node:
                return False
            i+=node.val
            if not node.right and not node.left and i==targetSum:
                return True
            return search(i,node.left) or search(i,node.right)
        return search(0,root)