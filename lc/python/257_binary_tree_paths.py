#!/usr/bin/python -t

# binary tree and dfs
# time O(n)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        ret = []

        self.helper(root, str(root.val), ret)
        
        return ret
    
    def helper(self, node, path, ret):
        if node.left == None and node.right == None:
            ret.append(path)
            return
        
        if node.left:
            self.helper(node.left, path+"->"+str(node.left.val), ret)

        if node.right:
            self.helper(node.right, path+"->"+str(node.right.val), ret)
            
        return

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        
        ret = []
        s = [(root, "")]
        
        while s:
            node, s_str = s.pop()
            if node.left == None and node.right == None:
                ret.append(s_str + str(node.val))
            if node.left:
                s.append((node.left, s_str+str(node.val)+"->"))
            if node.right:
                s.append((node.right, s_str+str(node.val) + "->"))

                
        return ret


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(root, path, ret):
            if root.left == None and root.right == None:
                ret.append(path)
                return
            
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val), ret)
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val), ret)
            
            return
        ret = []
        path = ""
        if root == None:
            return ret

        dfs(root, path + str(root.val), ret)

        return ret
