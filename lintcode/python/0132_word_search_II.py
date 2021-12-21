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
        
            

# dfs
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if len(words) == 0:
            return []
        maxLen = max(len(word) for word in words)
        ret = []
        path = ""
        v = set()
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        for i in range(len(board)):
            for j in range(len(board[0])):
                v.add((i, j))
                self.dfs(board, words, prefix_set, maxLen, i, j, board[i][j], v, ret)
                v.remove((i, j))

        return ret

    def dfs(self, board, words, prefix_set, maxLen, x, y, path, v, ret):
        if path not in prefix_set:
            return
        if len(path) > maxLen:
            return
        if path in words:
            if path not in ret:
                ret.append(path)
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(dirs)):
            nx = x + dirs[i][0]
            ny = y + dirs[i][1]

            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in v:
                v.add((nx, ny))
                self.dfs(board, words, prefix_set, maxLen, nx, ny, path+board[nx][ny], v, ret)
                v.remove((nx, ny))

        return

if __name__ == '__main__':
    s = Solution()
    a =["abce","sfcs","adee"]
    b= ["see","se"]
    print(s.wordSearchII(a,b))
