#!/usr/bin/python -t

# dp backpack

class Solution:
    """
    @param n: the number of tasks
    @param weights: the weight for every task
    @param tasks: the actual duration of every task
    @param p: maximum runtime for Pigeon in an hour
    @return: the maximum total weight that the Pigeon service can achieve in an hour
    """
    def maxWeight(self, n, weights, tasks, p):
        # write your code here
        # dp[i][j] means at ith tasks, the total weights of j minutes.
        p = p//2
        dp = [[0]*(p+1) for _ in range(len(tasks)+1)]
        for i in range(1, len(tasks)+1):
            for j in range(p+1):
                dp[i][j] = dp[i-1][j]
                if j >= tasks[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-tasks[i-1]]+weights[i-1])

        ret = 0
        for j in range(p, -1, -1):
            ret = max(ret, dp[len(tasks)][j])

        return ret 
