#!/usr/bin/python -t

#/*
# * 从n = 2开始递推，递推到n = 4的时候，4可以拆分成1和3或2和2
# * 那么3要不要继续拆分呢？2要不要继续拆分呢？
# * 不需要。因为我们已经把拆分2或3能得到的最大值分别计算好存在dp[2]和dp[3]了
# * 所以我们只需要比较2和dp[2]、3和dp[3]谁更大就知道要不要继续拆分
# * 所以对每个n，我们只需要考虑拆分成两个数a b的情况，然后看比较a和dp[a]
# * 以及b和dp[b]谁大就用谁相乘，如果dp[a]>a，表示dp[a]继续拆分能得到比不拆分
# * 更大的值，那么就拆分a，对于dp[b]和b也一样
# */

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [0] * (n+1)
        
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                l[i] = max(l[i], (max(j, l[j]) * max(i-j, l[i-j])))
                
        return l[n]


#java

        int[] dp = new int[n + 1];
        dp[0] = 1;
        int max = 0;
        for(int i = 1; i < n; i++){
            for(int j = i; j <= n; j++){
                dp[j] = Math.max(dp[j], dp[j - i] * i);
                if(j == n){
                    if(max < dp[j])
                        max = dp[j];
                }
            }
        }
        return max;
#This is a typical knapsack problem. We can assume that the volume of the knapsack is n. The items we can choose range from 1 to n - 1(because we must divide n into at least two positive parts). The point is that we can choose each item many times.
#The first loop means the items we can choose(i means first i items).
#And in the second loop, j means the sum of items that we are going to choose.
#For each item, we have two choices, pick it up or not. And we should choose the max result.
#just as dp[j] = Math.max(dp[j], dp[j - i] * i);
#Then, you are able to solve the problem.
#By the way, the initialization is also important.
