# dp
# time O(n^2)
# space O(n^2)

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * (2001) for _ in range(2001)]
        mark = dict()

        for i in range(n):
            mark[stones[i]] = i

        dp[0][0] = True
        for index in range(n):
            for prev_jump in range(n+1):
                if dp[index][prev_jump]:
                    if stones[index]+prev_jump in mark:
                        dp[mark[stones[index]+prev_jump]][prev_jump] = True
                    if stones[index]+prev_jump+1 in mark:
                        dp[mark[stones[index]+prev_jump+1]][prev_jump+1] = True
                    if stones[index]+prev_jump-1 in mark:
                        dp[mark[stones[index]+prev_jump-1]][prev_jump-1] = True

        for prev_jump in range(n+1):
            if dp[n-1][prev_jump] == True:
                return True

        return False

# dfs and memo

class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if stones[1] != 1:
            return False

        def dfs(i, k):
            if i == len(stones) - 1:
                return True

            if (i, k) in dp:
                 return dp[(i, k)]

            res = False
            for j in range(i + 1, len(stones)):
                if stones[i] + k == stones[j]:
                    res = res or dfs(j, k)
                if stones[i] + k + 1 == stones[j]:
                    res = res or dfs(j, k + 1)
                if stones[i] + k - 1 == stones[j]:
                    res = res or dfs(j, k - 1)

            dp[(i, k)] = res
            return res
        
        dp = {}
        return dfs(1, 1)


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        if len(stones) == 2:
            if stones[0] == 0 and stones[1] == 1:
                return True
        dp={}
        for stone in stones:
            dp[stone]=set()
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                if k-1>0 and stone+k-1 in dp:
                    dp[stone+k-1].add(k-1)
                if stone+k in dp:
                    dp[stone+k].add(k)
                if stone+k+1 in dp:
                    dp[stone+k+1].add(k+1)
        return len(dp[stones[-1]])>0
