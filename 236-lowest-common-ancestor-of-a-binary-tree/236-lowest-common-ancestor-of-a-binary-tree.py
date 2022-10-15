# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        leftsearch=self.lowestCommonAncestor(root.left,p,q)
        rightsearch=self.lowestCommonAncestor(root.right,p,q)
        if not leftsearch:
            return rightsearch
        if not rightsearch:
            return leftsearch
        return root