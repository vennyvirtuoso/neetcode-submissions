"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.mapp={}
    def clone(self,node):
        if node is None:
            return node
        if node in self.mapp:
            return self.mapp[node]
        temp=Node(node.val)
        self.mapp[node]=temp
        for node in node.neighbors:
            temp.neighbors.append(self.clone(node))
        return temp

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.clone(node)

