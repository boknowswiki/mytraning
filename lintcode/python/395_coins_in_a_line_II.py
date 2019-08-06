#!/usr/bin/python -t

#https://www.cnblogs.com/grandyang/p/5864323.html
#
#当我们处在i处时，我们有两种选择，拿一个还是拿两个硬币，我们现在分情况讨论：
#
#当我们只拿一个硬币values[i]时，那么对手有两种选择，拿一个硬币values[i+1]，或者拿两个硬币values[i+1] + values[i+2]
#a) 当对手只拿一个硬币values[i+1]时，我们只能从i+2到end之间来取硬币，所以我们能拿到的最大硬币数为dp[i+2]
#b) 当对手拿两个硬币values[i+1] + values[i+2]时，我们只能从i+3到end之间来取硬币，所以我们能拿到的最大硬币数为dp[i+3]
#由于对手的目的是让我们拿较小的硬币，所以我们只能拿dp[i+2]和dp[i+3]中较小的一个，所以对于我们只拿一个硬币的情况，我们能拿到的最大钱数为values[i] + min(dp[i+2], dp[i+3])
#
#当我们拿两个硬币values[i] + values[i + 1]时，那么对手有两种选择，拿一个硬币values[i+2]，或者拿两个硬币values[i+2] + values[i+3]
#a) 当对手只拿一个硬币values[i+2]时，我们只能从i+3到end之间来取硬币，所以我们能拿到的最大硬币数为dp[i+3]
#b) 当对手拿两个硬币values[i+2] + values[i+3]时，我们只能从i+4到end之间来取硬币，所以我们能拿到的最大硬币数为dp[i+4]
#由于对手的目的是让我们拿较小的硬币，所以我们只能拿dp[i+3]和dp[i+4]中较小的一个，所以对于我们只拿一个硬币的情况，我们能拿到的最大钱数为values[i] + values[i + 1] + min(dp[i+3], dp[i+4])
#
#综上所述，递推式就有了 dp[i] = max(values[i] + min(dp[i+2], dp[i+3]), values[i] + values[i + 1] + min(dp[i+3], dp[i+4]))

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        #长度小于2的时候第一个人一定获胜
        if n <= 2:
            return True
            
        dp = [0] * (n+1)

        #初始化，当到达最后3个数字时候，当作特例来处理
        #剩下0个元素，最大能拿到是0
        #剩下1个元素，最大能拿到是当前的那个元素
        #剩下2个元素，最大能拿到是2个都拿走
        #剩下3个元素，第三个肯定拿不到，那么拿到前2个
        dp[n] = 0
        dp[n-1] = values[n-1]
        dp[n-2] = values[n-1] + values[n-2]
        dp[n-3] = values[n-3] + values[n-2]
        
        #动态规划从大到小（从末尾开始，其实还是从小到大，所谓的小是剩下的硬币个数的小到大）
        for i in range(n-4, -1, -1):
            # take one coin or two coins
            dp[i] = max(values[i] + min(dp[i+2], dp[i+3]), values[i]+values[i+1]+min(dp[i+3], dp[i+4]))
            
        s = 0
        
        for v in values:
            s += v
            
        return s-dp[0] < dp[0]

