#!/usr/bin/python -t

# trie and dfs



class trie:
    def __init__(self, val="0"):
        self.val = val
        self.is_string=False
        self.left, self.right = None, None
        
    @classmethod
    def insert(cls, root, s):
        p = root
        
        for c in s:
            if c == "0":
                if p.left == None:
                    new_t = trie("0")
                    p.left = new_t
                p = p.left
            else:
                if p.right == None:
                    new_t = trie("1")
                    p.right = new_t
                p = p.right
                
        p.is_string=True
        return

class Solution:
    """
    @param s: the list of binary string
    @return: the max distance
    """
    def getAns(self, s):
        # Write your code here
        root = trie()
        for ss in s:
            trie.insert(root, ss)
        
        self.max_len = 0
        self.get_max_len(root)
        
        return self.max_len
        
        
    def get_max_len(self, root):  #字典树开始搜索
        if root is None:
            return 0
        #print root.val
        left_max_length = self.get_max_len(root.left)
        right_max_length = self.get_max_len(root.right)
        
        if root.left and root.right:
            self.max_len = max(self.max_len, left_max_length + right_max_length)
        
        if root.left and root.is_string:
            self.max_len = max(self.max_len, left_max_length)
        
        if root.right and root.is_string:
            self.max_len = max(self.max_len, right_max_length)
        #print left_max_length, right_max_length
        return max(left_max_length, right_max_length) + 1
