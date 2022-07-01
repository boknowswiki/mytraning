#!/usr/bin/python -t

# divid and conqur

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        
        if root == None:
            return []
            
        if root.left == None and root.right == None and root.val == target:
            return [[root.val]]
        
        ret = []    
        left = self.binaryTreePathSum(root.left, target-root.val)
        right = self.binaryTreePathSum(root.right, target-root.val)
        
        for i in left+right:
            ret.append([root.val] + i)
            
        return ret


# binary tree
# traverse way
# time O(n)
# space O(1)

class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        if not root:
            return []

        ret = []
        path = []

        self.helper(root, target, path, ret)

        return ret

    def helper(self, node, target, path, ret):
        if not node:
            return
        
        path.append(node.val)

        if node.left is None and node.right is None and target == node.val:
            ret.append(list(path))
            path.pop()
            return

        self.helper(node.left, target-node.val, path, ret)
        self.helper(node.right, target-node.val, path, ret)

        path.pop()
        
        return


# traversal way

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        path = [root.val]
        self.dfs(root, root.val, target, path, ret)
        
        return ret
        
    def dfs(self, node, val, target, path, ret):
        if node == None:
            return

        if node.left == None and node.right == None:
            if val == target:
                ret.append(path[:])
            return
        
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, val+node.left.val, target, path, ret)
            path.pop()
        
        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, val+node.right.val, target, path, ret)
            path.pop()
        
        return

# traversal way

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        self.dfs(root, 0, target, [], ret)
        
        return ret
        
    def dfs(self, node, val, target, path, ret):
        if node == None:
            return
        
        path.append(node.val)
        val += node.val
        
        if node.left == None and node.right == None and val == target:
            ret.append(path[:])
        
        self.dfs(node.left, val, target, path, ret)
        self.dfs(node.right, val, target, path, ret)
            
        path.pop()
        
        return



"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
            
        ret = []
        path = [root.val]
        self.dfs(root, target-root.val, path, ret)
        
        return ret
        
    def dfs(self, root, target, path, ret):
        if root == None:
            return
        
        if not root.left and not root.right:
            if target == 0:
                ret.append(list(path))
                return
            
        if root.left:
            path.append(root.left.val)
            self.dfs(root.left, target-root.left.val, path, ret)
            path.pop()
        if root.right:
            path.append(root.right.val)
            self.dfs(root.right, target-root.right.val, path, ret)
            path.pop()
        
        return
    
    
