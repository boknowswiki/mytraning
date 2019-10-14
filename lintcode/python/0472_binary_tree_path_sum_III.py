#!/usr/bin/python -t

# divid and conquer way

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        # write your code here
        A, B = self.helper(root, target)
        return B

    def helper(self, root, target):
        legit, pathto = [], []
        if root is None:
            return legit, pathto

        pathto.append([root.val])
        if root.val == target:
            legit.append([root.val])

        pathtol, legitl = self.helper(root.left, target)
        pathtor, legitr = self.helper(root.right, target)

        if len(pathtol) > 0:
            for path in pathtol:
                pathto.append(path+[root.val])
                if sum(path, root.val) == target:
                    a = path+[root.val]
                    legit.append(a)
                    legit.append(a[::-1])

        if len(pathtor) > 0:
            for path in pathtor:
                pathto.append(path+[root.val])
                if sum(path, root.val) == target:
                    b = path+[root.val]
                    legit.append(b)
                    legit.append(b[::-1])

        if len(pathtol) > 0 and len(pathtor) > 0:
            for i in pathtol:
                for j in pathtor:
                    if sum(j,sum(i, root.val)) == target:
                        c = i+[root.val]+j[::-1]
                        legit.append(c)
                        legit.append(c[::-1])

        legit = legit+legitl+legitr
        return pathto, legit

# dfs, traversal

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        # write your code here
        ret = []
        self.dfs(root, target, ret)
        
        return ret
        
    def dfs(self, node, target, ret):
        if node == None:
            return
        
        self.findsum(node, None, target, [], ret)
        
        self.dfs(node.left, target, ret)
        self.dfs(node.right, target, ret)
        
    def findsum(self, node, father, target, path, ret):
        if node == None:
            return
        path.append(node.val)
        target -= node.val
        
        if target == 0:
            ret.append(path[:])
            
        if node.parent not in [None, father]:
            self.findsum(node.parent, node, target, path, ret)
        if node.left not in [None, father]:
            self.findsum(node.left, node, target, path, ret)
        if node.right not in [None, father]:
            self.findsum(node.right, node, target, path, ret)
            
        path.pop()
        
        return

