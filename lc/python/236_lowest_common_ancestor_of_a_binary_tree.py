#!/usr/bin/python -t

# binary tree and dfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        self.get_path(root, p, [], p_path)
        q_path = []
        self.get_path(root, q, [], q_path)
        
        #print(f"p_path {p_path}, q_path {q_path}")
        
        return self.get_lca(p_path, q_path)
    
    def get_path(self, node, target, path, ret):
        if not node:
            return
        path.append(node)
        
        if node == target:
            ret.extend(list(path))
            return
        
        self.get_path(node.left, target, path, ret)
        self.get_path(node.right, target, path, ret)
        path.pop()
        
        return
    
    def get_lca(self, p1, p2):
        l1 = 0
        l2 = 0
        ret = None
        
        while l1 < len(p1) and l2 < len(p2):
            if p1[l1] == p2[l2]:
                ret = p1[l1]
                l1 += 1
                l2 += 1
            else:
                break
                
        return ret

class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
    
class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
    
#LCA Beizeng passed on lintcode, memory limit exceed in leetcode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.maxd = 0
        self.id = 0
        self.pmap = {}
        self.imap = {}
        self.dmap = {}
        self.parent = None
        
        if root == None:
            return None
        self.dfs(root, 0)
        
        self.parent = [[0] * (self.maxd) for _ in range(self.id)]
        self.getParent(root)
        
        #for i in range(1, self.maxd):
        #    for j in range(self.id):
        #        self.parent[j][i] = self.parent[self.parent[j][i-1]][i-1]
        for i in range(self.id):
            for j in range(1, self.maxd):
                self.parent[i][j] = self.parent[self.parent[i][j-1]][j-1]

        if p in self.pmap and q in self.pmap:
            return self.lca(p, q)
        else:
            return None
        
    def lca(self, p, q):
        id_p = self.pmap[p]
        id_q = self.pmap[q]
        
        if self.dmap[id_p] < self.dmap[id_q]:
            return self.lca(q, p)
        
        for i in range(self.maxd-1, -1, -1):
            if self.dmap[self.parent[id_p][i]] >= self.dmap[id_q]:
                id_p = self.parent[id_p][i]
                
            if self.dmap[id_p] == self.dmap[id_q]:
                break
            
        if id_p == id_q:
            return self.imap[id_p]
        
        for i in range(self.maxd-1, -1, -1):
            if self.imap[self.parent[id_p][i]] != self.imap[self.parent[id_q][i]]:
                id_p = self.parent[id_p][i]
                id_q = self.parent[id_q][i]
                
        return self.imap[self.parent[id_p][0]]
        
    def getParent(self, node):
        id_node = self.pmap[node]
        if node.left:
            id_left = self.pmap[node.left]
            self.parent[id_left][0] = id_node
            self.getParent(node.left)
            
        if node.right:
            id_right = self.pmap[node.right]
            self.parent[id_right][0] = id_node
            self.getParent(node.right)

        
    def dfs(self, node, depth):
        self.pmap[node] = self.id
        self.imap[self.id] = node
        self.dmap[self.id] = depth
        self.id = self.id + 1
        self.maxd = max(depth, self.maxd)
        
        if node.left:
            self.dfs(node.left, depth+1)
        if node.right:
            self.dfs(node.right, depth+1)
            
    

#LCA

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.depth = {}
        self.f = {}
        self.maxstep = 100

        self.depth[root.val] = 1
        if root.left:
            self.dfs(root, root.left)
        if root.right:
            self.dfs(root, root.right)
            
        c = self.lca(root.val, p.val, q.val)
        return TreeNode(c)
    
    def lca(self,root,m,n):
        if m==root or n==root:
            return root
        if self.depth[n]<self.depth[m]:
            temp = m
            m = n
            n = temp
        
        for i in range(len(self.f[n])):
            if self.depth[n]-self.depth[m]>=2**(len(self.f[n])-i-1):
                n = self.f[n][len(self.f[n])-i-1]
        if n==m:
            return n
        
        length = len(self.f[n])
        for i in range(length):
            if self.f[n][length-i-1]!=self.f[m][length-i-1]:
                n = self.f[n][length-i-1]
                m = self.f[m][length-i-1]
        return self.f[m][0]

    def dfs(self, prev, cur):
        self.f[cur.val] = [prev.val]
        self.depth[cur.val] = self.depth[prev.val]+1
        
        for i in range(1,self.maxstep):
            if  self.f[cur.val][i-1] in self.f.keys() and \
                len(self.f[self.f[cur.val][i-1]])>=i :
                self.f[cur.val].append(self.f[self.f[cur.val][i-1]][i-1])
            else:
                break
        if cur.left != None:
            self.dfs(cur, cur.left)
        if cur.right != None:
            self.dfs(cur, cur.right)

#Bei Zeng LCA
#from https://blog.csdn.net/weixin_42001089/article/details/83590686

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.f = {}
        self.vis = {}
        self.dfs(root)
        
        return self.tarjan(root, p.val, q.val)
    
    def tarjan(self, root, p, q):
        self.vis[root.val] = True
        if root.left:
            c = self.tarjan(root.left, p, q)
            if c != None:
                return c
            self.f[root.left.val] = root.val
        if root.right:
            c = self.tarjan(root.right, p, q)
            if c != None:
                return c
            self.f[root.right.val] = root.val
            
        if root.val == p and self.vis[q]:
            return self.find(q)
        if root.val == q and self.vis[p]:
            return self.find(p)
        
    def find(self, n):
        if n != self.f[n]:
            return self.find(self.f[n])
        else:
            return TreeNode(n)
        
    def dfs(self, node):
        if node:
            self.f[node.val] = node.val
            self.vis[node.val] = False
            self.dfs(node.left)
            self.dfs(node.right)
            


#time O(n) space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ret = None
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(node):
            if node == None:
                return False
            
            left = recurse_tree(node.left)
            right = recurse_tree(node.right)
            
            mid = node == p or node == q
            
            if mid + left + right >= 2:
                self.ret = node
                
            return mid or left or right
        
        recurse_tree(root)
        
        return self.ret


class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q


class Solution:

    # Three static flags to keep track of post-order traversal.

    # Both left and right traversal pending for a node.
    # Indicates the nodes children are yet to be traversed.
    BOTH_PENDING = 2
    # Left traversal done.
    LEFT_DONE = 1
    # Both left and right traversal done for a node.
    # Indicates the node can be popped off the stack.
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Initialize the stack with the root node.
        stack = [(root, Solution.BOTH_PENDING)]

        # This flag is set when either one of p or q is found.
        one_node_found = False

        # This is used to keep track of LCA index.
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:

            parent_node, parent_state = stack[-1]

            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            if parent_state != Solution.BOTH_DONE:

                # If both child traversals are pending
                if parent_state == Solution.BOTH_PENDING:

                    # Check if the current parent_node is either p or q.
                    if parent_node == p or parent_node == q:

                        # If one_node_found is set already, this means we have found both the nodes.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index.
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    child_node = parent_node.left
                else:
                    # traverse right child
                    child_node = parent_node.right

                # Update the node state at the top of the stack
                # Since we have visited one more child.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                # Add the child node to the stack for traversal.
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:

                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.

                # i.e. If LCA_index is equal to length of stack. Then we decrease LCA_index by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None
