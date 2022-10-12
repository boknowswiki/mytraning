#!/usr/bin/python -t

# binary tree and iterative way
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        st = []
        ret = []
        cur = root
        
        while cur != None:
            st.append(cur)
            #print(f"adding {cur.val} to st")
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
        
        while len(st) > 0:
            #print(f"len st {len(st)}")
            node = st.pop()
            ret.append(node.val)
            if st and st[-1].left == node:
                node = st[-1].right
                while node != None:
                    st.append(node)
                    if node.left:
                        node = node.left
                    else:
                        node = node.right
                        
        return ret
    

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ret = []
        self.helper(root, ret)
        
        return ret
    
    def helper(self, node, ret):
        if not node:
            return
        self.helper(node.left, ret)
        self.helper(node.right, ret)
        ret.append(node.val)
        
        return

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root == None:
            return ret
        stack = [root]

        while stack:
            node = stack.pop()
            if not isinstance(node, TreeNode):
                ret.append(node)
                continue
            stack.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)

        return ret

#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorder(root, ret):
            if root:
                postorder(root.left, ret)
                postorder(root.right, ret)
                ret.append(root.val)
                
            return
        
        ret = []
        postorder(root, ret)
        
        return ret
