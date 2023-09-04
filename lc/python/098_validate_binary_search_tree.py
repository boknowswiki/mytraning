#!/usr/bin/python -t

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        st = [(root, -sys.maxsize-1, sys.maxsize)]

        while st:
            cur, low, high = st.pop()
            if not cur:
                continue
            if cur.val <= low or cur.val >= high:
                return False

            st.append((cur.left, low, cur.val))
            st.append((cur.right, cur.val, high))

        return True

# binary tree and dfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.helper(root, -sys.maxsize-1, sys.maxsize)
    
    def helper(self, node, low, high):
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        return self.helper(node.left, low, node.val) and \
        self.helper(node.right, node.val, high)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        ret = []
        self.helper(root, ret)
        
        return self.increase(ret)
    
    def helper(self, node, ret):
        if not node:
            return
        
        self.helper(node.left, ret)
        ret.append(node.val)
        self.helper(node.right, ret)
        
        return
    
    def increase(self, ret):
        for i in range(1, len(ret)):
            if ret[i] <= ret[i-1]:
                return False
            
        return True

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#in-order traversal
class Solution(object):
    def __init__(self):
            self.prev = None
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ismonotomicincrease(r):
            if r == None:
                return True
            if ismonotomicincrease(r.left):
                if self.prev != None and self.prev.val >= r.val:
                    return False
                self.prev = r
                return ismonotomicincrease(r.right)

            return False

        if root == None:
            return True
        self.prev = None
        return ismonotomicincrease(root)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(r, low, high):
            if r == None:
                return True
            return (low == None or r.val > low) and \
                    (high == None or r.val < high) and \
                    valid(r.left, low, r.val) and \
                    valid(r.right, r.val, high)

        if root == None:
            return True

        return valid(root, None, None)  

#BFS
#time O(n) space O(n)

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
