#!/usr/bin/python -t

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def serialize(self, root):
        if not root:
            return ""
        res = []
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else: 
                    res.append('#')
                
        return ",".join(res)

    def deserialize(self, data):
        nodes = data.split(',')
        if not nodes:
            return None
        if nodes[0] != "#":
            
            root = TreeNode(int(nodes.pop(0)))
            queue = [root]
        
        while queue:
            node = queue.pop(0)
            if nodes:
                left_node = nodes.pop(0)
                if left_node != "#":
                    node.left = TreeNode(int(left_node))
                    queue.append(node.left)
            if nodes:
                right_node = nodes.pop(0)
                if right_node != "#":
                    node.right = TreeNode(int(right_node))
                    queue.append(node.right)
        return root
