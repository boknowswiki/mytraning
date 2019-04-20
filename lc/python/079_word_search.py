#!/usr/bin/python -t

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

