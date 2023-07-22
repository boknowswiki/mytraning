
# dp
# time O(k*n^2)
# space O(k*n^2)

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directs = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        dp = [[[0]*n for _ in range(n)] for _ in range(k+1)]
        dp[0][row][column] = 1

        for moves in range(1, k+1):
            for i in range(n):
                for j in range(n):
                    for di, dj in directs:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni <n and 0 <= nj < n:
                            dp[moves][i][j] += dp[moves-1][ni][nj]

                    dp[moves][i][j] /= 8

        ret = sum(dp[k][i][j] for i in range(n) for j in range(n))

        return ret
