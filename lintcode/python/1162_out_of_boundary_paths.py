#!/usr/bin/python -t

class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param N: an integer
    @param i: an integer
    @param j: an integer
    @return: the number of paths to move the ball out of grid boundary
    """
    def findPaths(self, m, n, N, i, j):
        # Write your code here
        self.memoryHashmap = {}
        mod = (10 ** 9 + 7)
        
        output = self.findPathsDfs(m, n, N, i, j)
        
        return output % mod
        
    def findPathsDfs(self, m, n, N, i, j):
        if (i, j, N) in self.memoryHashmap:
            return self.memoryHashmap[(i, j, N)]
        
        if self.isOutOfBoundary(m, n, i, j):
            return 1
        
        if N == 0:
            return 0
            
        total = 0
        # go up
        total += self.findPathsDfs(m, n, N-1, i-1, j)
        # go down
        total += self.findPathsDfs(m, n, N-1, i+1, j);
        # go left
        total += self.findPathsDfs(m, n, N-1, i, j-1);
        # go right
        total += self.findPathsDfs(m, n, N-1, i, j+1);
        
        # update table
        self.memoryHashmap[(i,j,N)] = total
        
        return total
        
    def isOutOfBoundary(self, m, n, i, j):
        if i < 0 or j < 0 or i > m - 1 or j > n - 1:
            return True
        return False

class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param N: an integer
    @param i: an integer
    @param j: an integer
    @return: the number of paths to move the ball out of grid boundary
    """
    def findPaths(self, m, n, N, i, j):
        # Write your code here
        MOD = 10**9 + 7
        dz = zip((1, 0, -1, 0), (0, 1, 0, -1))
        dp = [[0] *n for x in range(m)]
        dp[i][j] = 1
        ans = 0
        for t in range(N):
            ndp = [[0] *n for x in range(m)]
            for x in range(m):
                for y in range(n):
                    for dx, dy in dz:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            ndp[nx][ny] = (ndp[nx][ny] + dp[x][y]) % MOD
                        else:
                            ans = (ans + dp[x][y]) % MOD
            dp = ndp
        return ans


# dp solution, TLE

class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param N: an integer
    @param i: an integer
    @param j: an integer
    @return: the number of paths to move the ball out of grid boundary
    """
    def findPaths(self, m, n, N, i, j):
        # Write your code here
        if N == 0:
            return 0
            
        mem = {}
        def dfs(m, n, N, step, i, j):
            if (i, j, step) in mem:
                return mem[(i,j,step)]
                
            if not (0<=i<m and 0<=j<n):
                return 1
                
            if step == N:
                return 0
                
            ret = 0
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = i+dx
                y = j+dy
                ret += dfs(m, n, N, step+1, x, y)
            mem[(x,y, step)] = ret
            return ret
        
        MOD = 1000000007
        
        ret = 0
        ret = dfs(m, n, N, 0, i, j)
        return ret%MOD

