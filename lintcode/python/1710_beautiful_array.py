#!/usr/bin/python -t

# 首先明确一下，如果一个数组X是漂亮数组
# 
# 那么2X(每个元素乘以2)，也是漂亮数组
# 那么2X-1(每个元素乘以2，减一)，也是漂亮数组
# 满足下面条件的为漂亮数组：每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]
# 
# 由于奇数+偶数 = 奇数
# 2* [奇数或偶数] = 偶数
# 因此，首先奇偶数分开，分成两部分，那么这两部分就满足这个条件，奇数部分为X，偶数部分为Y
# 然后对X进行拆分，将X的所有位向右移动一位，然后拆分奇偶
# 
# 对Y进行拆分，将Y的所有位向右移动一位，然后拆分奇偶

class Solution:
    """
    @param N: an integer
    @return: return any beautiful array A
    """
    def beautifulArray(self, N):
        # write your code here.
        memo = {1: [1]}
        def f(N):
            if N not in memo:
                odds = f((N+1)/2)
                evens = f(N/2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[N]
        return f(N)
