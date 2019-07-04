#!/usr/bin/python -t

#time O(n) for initial build tree, update O(logn), query O(logn)
#space O(n)


class node(object):
    def __init__(self, start, end, t=0):
        self.start = start
        self.end = end
        self.t = t
        self.left = self.right = None
        

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.root = self.build(0, len(self.nums)-1)
        
    def build(self, start, end):
        if start > end:
            return None
        if start == end:
            return node(start, end, self.nums[start])
        
        mid = (end-start)/2 + start
        left = self.build(start, mid)
        right = self.build(mid+1, end)
            
        root = node(start, end)
        root.left = left
        root.right = right
        root.t = root.left.t + root.right.t
        
        return root

    def updateval(self, root, i , val):
        if root.start == root.end:
            root.t = val
            return val
    
        mid = (root.end - root.start)/2 + root.start
        
        if i <= mid:
            self.updateval(root.left, i ,val)
        else:
            self.updateval(root.right, i, val)
            
        root.t = root.left.t + root.right.t
        
        return root.t
    
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        return self.updateval(self.root, i, val)
        
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.t
                
        mid = (root.end - root.start)/2 + root.start
        
        if end <= mid:
            return self.query(root.left, start, end)
        elif start >= mid+1:
            return self.query(root.right, start, end)
        else:
            return self.query(root.left, start, root.left.end) + \
                              self.query(root.right, root.right.start, end)
   

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


class NumArray(object):

    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0]*self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
    
    def update(self, i, val):
        n = self.l + i
        self.tree[n] = val
        while n > 1:
            self.tree[n>>1] = self.tree[n] + self.tree[n^1]
            n >>= 1
        
    
    def sumRange(self, i, j):
        m = self.l + i
        n = self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 ==0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res
