# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ma=collections.defaultdict(int)
        def mode(node):
            if not node:
                return
            ma[node.val]=1+ma.get(node.val,0)
            mode(node.left)
            mode(node.right)
        mode(root)
        x=max(ma.values())
        res=[]
        for i in ma:
            if ma[i]==x:
                res.append(i)
        return res