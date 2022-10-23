"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        q=collections.deque()
        seen=dict()
        if not node:
            return node
        copy=Node(node.val)
        q.append(node)
        seen[node]=copy
        while q:
            copy=q.popleft()
            for nei in copy.neighbors:
                if nei not in seen:
                    seen[nei]=Node(nei.val)
                    q.append(nei)
                seen[copy].neighbors.append(seen[nei])
        return seen[node]