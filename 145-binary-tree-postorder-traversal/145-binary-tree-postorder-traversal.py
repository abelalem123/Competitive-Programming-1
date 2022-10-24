# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def search1(node):
            if not node:
                return
            search1(node.left)
            search1(node.right)
            res.append(node.val)
#         def search(root):
#             q=collections.deque()
#             q.append(too)
#             while q:
#                 node=
#                 while node.left:
#                     node=node.left
                    
#                 while node.right:
#                     node=node.right
                    
#                 res.append(node)
        search1(root)
        return res
        