#!/usr/bin/python -t

# tire + dfs。
# 字典树用于前缀查找。
# dfs用于搜索，
# 找到单词时搜索下一个单词
# 没有搜索到单词时，四方向遍历（回溯 + 标记）


class TrieNode(object):
    def __init__(self, value=0):
        self.value = value
        self.isWord = False
        self.children = collections.OrderedDict()
    #建树
    @classmethod
    def insert(cls, root, word):
        p = root
        for c in word:
            child = p.children.get(c)
            if not child:
                child = TrieNode(c)
                p.children[c] = child
            p = child

        p.isWord = True

class Solution:
    """
    @param: board: a list of lists of character
    @param: words: a list of string
    @return: an integer
    """
    def boggleGame(self, board, words):
        # write your code here
        self.board = board
        self.words = words
        self.m = len(board)
        self.n = len(board[0])
        self.results = []
        self.temp = []
        self.visited = [[False for _ in xrange(self.n)] for _ in xrange(self.m)]
        
        self.root = TrieNode()
        for word in words:
            TrieNode.insert(self.root, word)
        
        self.dfs(0, 0, self.root)
                
        return len(self.results)
    #dfs查找单词
    def dfs(self, x, y, root):
        for i in xrange(x, self.m):
            for j in xrange(y, self.n):
                paths = []
                temp = []
                self.getAllPaths(i, j, paths, temp, root)
                for path in paths:
                    word = ''
                    for px, py in path:
                        word += self.board[px][py]
                        self.visited[px][py] = True
                    self.temp.append(word)
                    
                    if len(self.temp) > len(self.results):
                        self.results = self.temp[:]
                        
                    self.dfs(i, j, root)
                    self.temp.pop()
                    for px, py in path:
                        self.visited[px][py] = False
            y = 0
    
    def getAllPaths(self, i, j, paths, temp, root):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or \
            self.board[i][j] not in root.children or \
            self.visited[i][j] == True:
            return
        
        root = root.children[self.board[i][j]]
        if root.isWord:
            temp.append((i,j))
            paths.append(temp[:])
            temp.pop()
            return
        #四方向查找
        self.visited[i][j] = True
        deltas = [(0,1), (0,-1), (1,0), (-1, 0)]
        for dx, dy in deltas:
            newx = i + dx
            newy = j + dy
            temp.append((i,j))
            self.getAllPaths(newx, newy, paths, temp, root)
            temp.pop()
        self.visited[i][j] = False
