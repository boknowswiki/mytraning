#!/usr/bin/python -t

# trie

class trieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        
class trie:
    def __init__(self):
        self.root = trieNode()
        
    def insert(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
            
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word
        
        return
    
    def find(self, word):
        cur = self.root
        
        for c in word:
            cur = cur.children.get(c)
            if cur == None:
                return None
        return cur
        

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        if n == 0:
            return []
            
        t = trie()
        
        for w in words:
            t.insert(w)
            
        ret = set()
        #v = set()
        
        for i in range(m):
            for j in range(n):
                self.search(board, i, j, t.root.children.get(board[i][j]), set([(i,j)]), ret)
                #v.remove((i, j))
                
        return list(ret)
        
    def search(self, board, x, y, node, v, ret):
        if node == None:
            return
        if node.is_word:
            ret.add(node.word)
            
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            
            if not self.valid(board, cx, cy, v):
                continue
            v.add((cx, cy))
            self.search(board, cx, cy, node.children.get(board[cx][cy]), v, ret)
            v.remove((cx, cy))
            
        return
    
    def valid(self, board, x, y, v):
        m, n = len(board), len(board[0])
        
        #print v
        if x < 0 or y < 0 or x >= m or y >= n or (x,y) in v:
            return False
        return True
        
            
