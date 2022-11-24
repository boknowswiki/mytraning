# trie and dfs

class trie:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.ref = 0
        
    def add(self, word):
        cur = self
        cur.ref += 1
        for w in word:
            if w not in cur.children:
                cur.children[w] = trie()
            cur = cur.children[w]
            cur.ref += 1
        cur.is_word = True
    
    def remove(self, word):
        cur = self
        cur.ref -= 1
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
                cur.ref -= 1   
        cur.is_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = trie()
        for word in words:
            root.add(word)
        m, n = len(board), len(board[0])
        ret = []
        v = set()
        
        def dfs(x, y, node, path):
            if (
                x not in range(m) or
                y not in range(n) or
                board[x][y] not in node.children or
                node.children[board[x][y]].ref < 1 or
                (x, y) in v
            ):
                return
            
            v.add((x, y))
            path += board[x][y]
            node = node.children[board[x][y]]
            if node.is_word:
                ret.append(path)
                root.remove(path)

            dfs(x+1, y, node, path)
            dfs(x-1, y, node, path)
            dfs(x, y+1, node, path)
            dfs(x, y-1, node, path)
            v.remove((x, y))
            
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
                
        return ret

# trie and dfs
# reference: https://github.com/neetcode-gh/leetcode/blob/main/python/212-Word-Search-II.py

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r not in range(ROWS) 
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)        

# trie and dfs
# reference: https://leetcode.com/problems/word-search-ii/discuss/2041937/Python-DFS-%2B-Trie-(99)-with-Trie-optimization

class Trie(collections.defaultdict):
    def __init__(self):
        super().__init__(lambda: Trie())
        self._is_word = False
        self._count = 0
    
    def add(self, word):
        runner = self
        runner._count += 1
        for c in word:
            runner = runner[c]
            runner._count += 1
        runner._is_word = True
        
    def remove(self, word):
        runner = self
        runner._count -= 1
        for c in word:
            if runner[c]._count == 1:
                del runner[c]
                return
            runner = runner[c]
            runner._count -= 1
        runner._is_word = False
        
    def contains(self, word):
        runner = self
        for c in word:
            if runner._count == 0 or c not in runner:
                return False
            runner = runner[c]
        return runner._is_word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        root = Trie()
        for word in words:
            root.add(word)
            
        def dfs(i, j, trie, s):
            s.append(board[i][j])
            trie = trie[board[i][j]]
            if trie._is_word:
                root.remove(s)
                trie._is_word = False
                res.append("".join(s))

            board[i][j] = '#'
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] in trie:
                    dfs(ni, nj, trie, s)
            board[i][j] = s.pop()
                
        res = []    
        for i in range(n):
            for j in range(m):
                if board[i][j] in root:
                    dfs(i, j, root, [])
                 
        return res
        
