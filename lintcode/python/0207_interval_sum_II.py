class segTree:
    def __init__(self, start, end, total=0):
        self.start = start
        self.end = end
        self.total = total
        self.left = self.right = None
        
    @classmethod
    def build(cls, start, end, s):
        if start > end:
            return
        if start == end:
            return segTree(start, end, s[start])
            
        node = segTree(start, end, s[start])
        mid = (start+end)/2
        node.left = cls.build(start, mid, s)
        node.right = cls.build(mid+1, end, s)
        node.total = node.left.total + node.right.total
        
        return node
    @classmethod
    def query(cls, root, start, end):
        if root.start > end or root.end < start:
            return 0
        if start <= root.start and root.end <= end:
            return root.total
            
        return (cls.query(root.left, start, end)+cls.query(root.right, start, end))
        
    @classmethod
    def modify(cls, root, index, val):
        if root == None:
            return
        if root.start == root.end:
            root.total = val
            return
        
        if root.left.end >= index:
            cls.modify(root.left, index, val)
        else:
            cls.modify(root.right, index, val)
            
        root.total = root.left.total + root.right.total
        
        return
            
        

class Solution:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        # do intialization if necessary
        self.root = segTree.build(0, len(A)-1, A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        # write your code here
        return segTree.query(self.root, start, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        # write your code here
        segTree.modify(self.root, index, value)
        return
