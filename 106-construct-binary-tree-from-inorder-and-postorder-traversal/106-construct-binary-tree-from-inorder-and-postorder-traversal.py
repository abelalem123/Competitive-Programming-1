# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        node=TreeNode(postorder[-1])
        sep=inorder.index(postorder[-1]) #1
        node.left=self.buildTree(inorder[:sep],postorder[:sep])
        node.right=self.buildTree(inorder[sep+1:],postorder[sep:-1])
        return node