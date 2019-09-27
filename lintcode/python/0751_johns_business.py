#!/usr/bin/python -t

#segment tree AC

class Solution:
    
    class SegmentTreeNode:
        def __init__(self, start, end, min):
            self.start, self.end, self.min = start, end, min
            self.left, self.right = None, None
    
    def buildTree(self, start, end, A):
        if start > end:
            return None

        node = self.SegmentTreeNode(start, end, A[start])
        if start == end:
            return node

        mid = (start + end) / 2
        node.left = self.buildTree(start, mid, A)
        node.right = self.buildTree(mid + 1, end, A)
        if node.left is not None and node.left.min < node.min:
            node.min = node.left.min
        if node.right is not None and node.right.min < node.min:
            node.min = node.right.min
        return node
    
    def query(self, root, start, end):
        if root.start > end or root.end < start:
            return 0xffffff
    
        if start <= root.start and root.end <= end:
            return root.min
        
        ans = 0xffffff
        
        if root.left is not None:
            ans = min(ans, self.query(root.left, start, end))
        
        if root.right is not None:
            ans = min(ans, self.query(root.right, start, end))
        
        
        return ans
    
  
    """
    @param A: The prices [i]
    @param k: 
    @return: The ans array
    """
    def business(self, A, k):
        root = self.buildTree(0, len(A)-1, A)
        ans = []
        for i in range(len(A)):
            l = i - k
            r = i + k
            if l < 0:
                l = 0
            if r > len(A) - 1:
                r = len(A) - 1
            tmp = A[i] - self.query(root, l, r)
            ans.append(tmp)
        return ans

#segment tree solution, TLE

class segTreeNode():
    def __init__(self, start, end, m):
        self.start, self.end, self.m = start, end, m
        self.left, self.right = None, None

class Solution:
    """
    @param A: The prices [i]
    @param k: 
    @return: The ans array
    """
    def build(self, A, start, end):
        if start > end:
            return None
            
        node = segTreeNode(start, end, A[start])
        
        if start == end:
            return node
            
        mid = (start+end)/2
        node.left = self.build(A, start, mid)
        node.right = self.build(A, mid+1, end)
        node.m = min(node.left.m, node.right.m)
        return node
        
    def query(self, root, start, end):
        if start > end or root == None:
            return 0x7fffff
        if start <= root.start and root.end <= end:
            return root.m
            
        return min(self.query(root.left, start, end), self.query(root.right, start, end))
    
    def business(self, A, k):
        #
        n = len(A)
        
        root = self.build(A, 0, n-1)
        ret = []
        
        for i in range(n):
            l = i-k if i-k >= 0 else 0
            r = i+k if i+k <= n-1 else n-1
            ret.append(A[i] - self.query(root, l, r))
            
        return ret

