#!/usr/bin/python -t


# dfs

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        m = len(board)
        n = len(board[0])

        v = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    v.add((i, j))
                    if self.dfs(board, i, j, v, 1, word):
                        return True
                    v.remove((i, j))

        return False

    def dfs(self, board, x, y, v, index, word):
        if index == len(word):
            return True

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for k in range(len(dirs)):
            nx = dirs[k][0] + x
            ny = dirs[k][1] + y
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in v and board[nx][ny] == word[index]:
                v.add((nx, ny))
                if self.dfs(board, nx, ny, v, index+1, word):
                    return True
                v.remove((nx,ny))

        return False


if __name__ == '__main__':
    s = Solution()
    a = ["ABCE","SFES","ADEE"]
    b = "ABCESEEEFS"
    print(s.exist(a,b))

# dfs and backtracking

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        m = len(board)
        if m == 0:
            return False
            
        n = len(board[0])
        if n == 0:
            return False
        v = set()
        
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, m, n, v):
                    return True
                    
        return False
        
    def dfs(self, board, word, x, y, m, n, v):
        if word == '':
            return True
        if x < 0 or x >= m or y < 0 or y >=n:
            return False
        
        if word[0] == board[x][y] and (x, y) not in v:
            v.add((x, y))
            if self.dfs(board, word[1:], x+1, y, m, n, v) or self.dfs(board, word[1:], x-1, y, m, n, v) or \
                self.dfs(board, word[1:], x, y+1, m, n, v) or self.dfs(board, word[1:], x, y-1, m, n, v):
                    return True
            else:
                v.remove((x, y))
                
        return False
