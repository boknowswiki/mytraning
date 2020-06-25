#!/usr/bin/python -t

# 使用排列式搜索 + Trie

# time O(n^k)

class trieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.wl = []
        
class trie:
    def __init__(self):
        self.root = trieNode()
        
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
            cur = cur.children[c]
            cur.wl.append(word)
        cur.is_word = True

        return
    
    def find(self, word):
        cur = self.root
        for c in word:
            cur = cur.children.get(c)
            if cur == None:
                return None
        return cur
        
    def get_words_with_prefix(self, prefix):
        cur = self.find(prefix)
        
        return cur if cur == None else cur.wl
        
    def contains(self, word):
        cur = self.find(word)
        
        return cur is not None and cur.is_word
        

class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        t = trie()
        for word in words:
            t.insert(word)
            
        ret = []
        
        for word in words:
            self.dfs(t, [word], ret)
            
        return ret
        
    def dfs(self, t, path, ret):
        n = len(path[0])
        curt_index = len(path)
        if curt_index == n:
            ret.append(list(path))
            return
        
        for row_index in range(curt_index, n):
            prefix = ''.join([path[i][row_index] for i in range(curt_index)])
            #print path, curt_index, prefix
            if t.find(prefix) is None:
                return
        
        prefix = ''.join([path[i][curt_index] for i in range(curt_index)])
        for word in t.get_words_with_prefix(prefix):
            path.append(word)
            self.dfs(t, path, ret)
            path.pop() # remove the last word        
        
        
