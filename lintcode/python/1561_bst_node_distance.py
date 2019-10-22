#!/usr/bin/python -t

class Solution:
    """
    @param numbers: the given list
    @param node1: the given node1
    @param node2: the given node2
    @return: the distance between two nodes
    """
    def bstDistance(self, numbers, node1, node2):
        # Write your code here
        
        def find (nums, target):
            l , r = float("-inf"), float("inf")
            p = []
            for i in nums:
                if l < i < r:
                    p.append(i)
                    if i == target:
                        return p
                    elif i < target:
                        l = i
                    else:
                        r = i
            return []
        n1, n2 = find(numbers, node1) , find(numbers, node2)
        c = 0
        if not n1 or not n2:
            return -1
        for i in range(min(len(n1), len(n2))):
            if n1[i] == n2[i]:
                c += 1
        
        return len(n1) + len(n2) - 2 * c

#BST也就是二叉搜索树，也就是保证一个节点的左子树的点都小于它，右子树的点都大于它。本题也就是BST的基本建立和递归查询问题。查询的时候注意先判断节点是否存在。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param numbers: the given list
    @param node1: the given node1
    @param node2: the given node2
    @return: the distance between two nodes
    """
    
    def check(self, nums, n1, n2):
        s = set()
        
        for num in nums:
            s.add(num)
            
        if n1 in s and n2 in s:
            return True
        return False
        
    def insert(self, root, val):
        if root == None:
            return TreeNode(val)
            
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
            
        return root
        
    def build(self, nums):
        if len(nums) == 0:
            return None
            
        root = TreeNode(nums[0])
        n = len(nums)
        
        for i in range(1, n):
            self.insert(root, nums[i])
            
        return root
        
    def findDis(self, root, val):
        dis = 0
        while root.val != val:
            dis += 1
            
            if root.val < val:
                root = root.right
            else:
                root = root.left
                
        return dis
        
    def bstDistance(self, numbers, node1, node2):
        # Write your code here
        if not numbers or len(numbers) < 2:
            return -1
            
        if not self.check(numbers, node1, node2):
            return -1
            
        root = self.build(numbers)
        
        while node1 > root.val and node2 > root.val or node1 < root.val and node2 < root.val:
            if node1 > root.val and node2 > root.val:
                root = root.right
            else:
                root = root.left
                
        return self.findDis(root, node1) + self.findDis(root, node2)
        

