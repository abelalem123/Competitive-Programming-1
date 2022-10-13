# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sametree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def sametree(self,oak,weira):
        if not oak and not weira:
            return True
        if oak and weira and oak.val==weira.val:
            return  (self.sametree(oak.right,weira.right) 
                    and self.sametree(oak.left,weira.left))
        return False
        