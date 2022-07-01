#!/usr/bin/python -t

# binary tree
# divid and conquer way
# time O(n)
# space O(1)


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        # write your code here
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        left = self.helper(str(root.val), root.left)
        right = self.helper(str(root.val), root.right)

        print(f"left {left}, right {right}")
        left.extend(right)
        return left


    def helper(self, path, node):
        print(f"{path}")
        if node is None:
            return []

        new_path = path + "->" + str(node.val)
        if node.left is None and node.right is None:
            return [new_path]

        left = self.helper(new_path, node.left)
        right = self.helper(new_path, node.right)

        left.extend(right)
        return left

# dfs with divid and conquer solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        if root.left == None and root.right == None:
            #return ret.append(str(root.val))
            return [str(root.val)]
            
        l_paths = self.binaryTreePaths(root.left)
        r_paths = self.binaryTreePaths(root.right)
        
        for path in l_paths + r_paths:
            ret.append(str(root.val) + '->' + path)
            
        return ret

# dfs recursive traversal tree solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
            
        self.helper(root, str(root.val), ret)
        
        return ret
    

    def helper(self, root, path, ret):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            ret.append(path)
            
        if root.left:
            self.helper(root.left, path + "->" + str(root.left.val), ret)
        if root.right:
            self.helper(root.right, path + "->" + str(root.right.val), ret)
            
        return

