#!/usr/bin/python -t

# segment tree solution

class segtree:
    def __init__(self, start, end, cnt):
        self.start = start
        self.end = end
        self.cnt = cnt
        self.left, self.right = None, None
    

class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def build(self, start, end, s):
        if start > end:
            return None
        
        if start == end:
            return segtree(start, end, 0)
            
        node = segtree(start, end, 0)
        mid = (start+end)/2
        node.left = self.build(start, mid, 0)
        node.right = self.build(mid+1, end, 0)
        
        return node
        
    def modify(self, root, index, val):
        if root == None:
            return
        
        if root.start == root.end and root.start == index:
            root.cnt += val
            return
        
        if root.left.end >= index:
            self.modify(root.left, index, val)
        else:
            self.modify(root.right, index, val)

        root.cnt = root.left.cnt + root.right.cnt
            
    def query(self, root, start, end):
        if start > root.end or end < root.start:
            return 0
            
        if start <= root.start and root.end <= end:
            return root.cnt
            
        return self.query(root.left, start, end)+self.query(root.right, start, end)
        
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        root = self.build(0, 10000, 0)
        
        for a in A:
            self.modify(root, a, 1)
            
        ret = []
        for q in queries:
            ret.append(self.query(root, 0, q-1))
            
        return ret

if __name__ == '__main__':
    s = [1,2,3,4,5,6]
    t = [1,2,3,4]
    ss = Solution()
    print "answer is\n"
    print ss.countOfSmallerNumber(s, t)

