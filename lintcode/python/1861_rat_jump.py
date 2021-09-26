#!/usr/bin/python -t

# dp

# https://www.lintcode.com/problem/1861/solution/32932?_from=collection&fromId=160

class Solution:
    """
    @param arr: the steps whether have glue
    @return: the sum of the answers
    """
    def ratJump(self, arr):
        # Write your code here.
        # dp[i][0/1] defines steps at ith stair with even or odd number.
        MOD = 1000000007
        # 楼梯有无胶水的状态是从高往低输入的

        # arr长度
        n = len(arr)

        # 初始化dp数组
        # dp[i][0] even
        # dp[i][1] odd

        dp = [[0] * 2 for i in range(n + 10)]

        # 边界条件
        dp[0][0] = 1

        # 奇数偶数次分别能跳的数量
        odd = [1, 2, 4]
        even = [1, 3, 4]

        # 枚举状态dp[i][0] dp[i][1]

        for i in range(n - 1):

            # 枚举转移，这一步跳几个台阶
            for j in range(3):

                # 1能直接跳下来，若超过地面，也算是可以到达
                # 2不能直接跳下来的话 要跳到没有胶水的地方

                if i + odd[j] >= n or arr[i + odd[j]] == 0:
                    dp[i + odd[j]][1] += dp[i][0]
                    dp[i + odd[j]][1] %= MOD
                if i + even[j] >= n or arr[i + even[j]] == 0:
                    dp[i + even[j]][0] += dp[i][1]
                    dp[i + even[j]][0] %= MOD
                # 枚举统计跳到地面或者地面再往下的答案 
                ans = 0
        for i in range(n - 1, n + 4):
            ans = (ans + dp[i][0] + dp[i][1]) % MOD
        return (int)(ans)
