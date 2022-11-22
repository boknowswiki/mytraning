#!/usr/bin/python -t

# dfs and backtracking
# referecne: https://leetcode.com/problems/word-search/discuss/2439953/Python-or-Faster-than-98-w-Proof-or-Easy-to-Understand
# lots of the solution gets Time Limit Exceeded

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Count number of letters in board and store it in a dictionary
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1

        # Count number of letters in word
        # Check if board has all the letters in the word and they are atleast same count from word
        wordDic = Counter(word)
        for c in wordDic:
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False

        # Traverse through board and if word[0] == board[i][j], call the DFS function
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, board, word):
                        return True

        return False

    def dfs(self, i, j, k, board, word):
        # Recursion will return False if (i,j) is out of bounds or board[i][j] != word[k] which is current letter we need
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or \
           k >= len(word) or word[k] != board[i][j]:
            return False

        # If this statement is true then it means we have reach the last letter in the word so we can return True
        if k == len(word) - 1:
            return True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in directions:
            # Since we can't use the same letter twice, I'm changing current board[i][j] to -1 before traversing further
            tmp = board[i][j]
            board[i][j] = -1

            # If dfs returns True then return True so there will be no further dfs
            if self.dfs(i + x, j + y, k + 1, board, word): 
                return True

            board[i][j] = tmp

#time O(n^2) space O(mn)

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        visit = [0] * m
        for i in range(m):
            visit[i] = [0]*n
            
        def dfs(board, word, cur, r, c, visit, m, n):
            if cur == len(word):
                return True
            
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            if board[r][c] != word[cur]:
                return False
            if visit[r][c] == 1:
                return False
            
            visit[r][c] = 1
            
            ret = dfs(board, word, cur+1, r-1, c, visit, m, n) or \
                    dfs(board, word, cur+1, r+1, c, visit, m, n) or \
                    dfs(board, word, cur+1, r, c-1, visit, m, n) or  \
                    dfs(board, word, cur+1, r, c+1, visit, m, n)
                    
            visit[r][c] = 0
            
            return ret
            
        for i in range(m):
            for j in range(n):
                if (dfs(board, word, 0, i, j, visit, m, n)):
                    return True
        return False
            
if __name__ =='__main__':
    s = Solution()
    #print('%d\n' % (s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")))
    #print('%d\n' % (s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")))
    print('%d\n' % (s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "AB")))

