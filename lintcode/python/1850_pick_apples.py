#!/usr/bin/python -t

# prefix sum

class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def PickApples(self, A, K, L):
        # write your code here
        n = len(A)
        if n < K+L:
            return -1

        pre_sum = A[:]
        for i in range(1, n):
            pre_sum[i] += pre_sum[i-1]

        # max sum before i.
        pre_k = [0]*n
        pre_l = [0]*n
        # max sum after i.
        post_k = [0]*n
        post_l = [0]*n

        for i in range(n):
            if i == K-1:
                pre_k[i] = self.range_sum(pre_sum, i-K+1, i)
            elif i > K-1:
                pre_k[i] = max(self.range_sum(pre_sum, i-K+1, i), pre_k[i-1])
            if i == L-1:
                pre_l[i] = self.range_sum(pre_sum, i-L+1, i)
            elif i > L-1:
                pre_l[i] = max(self.range_sum(pre_sum, i-L+1, i), pre_l[i-1])

        for i in range(n-1, -1, -1):
            if i+K-1 == n-1:
                post_k[i] = self.range_sum(pre_sum, i, i+K-1)
            elif i+K-1 < n-1:
                post_k[i] = max(self.range_sum(pre_sum, i, i+K-1), post_k[i+1])
            if i+L-1 == n-1:
                post_l[i] = self.range_sum(pre_sum, i, i+L-1)
            elif i+L-1 < n-1:
                post_l[i] = max(self.range_sum(pre_sum, i, i+L-1), post_l[i+1])

        ret = 0
        for i in range(1, n-1):
            ret = max(ret, pre_k[i]+post_l[i+1])
            ret = max(ret, pre_l[i]+post_k[i+1])
        
        return ret

    def range_sum(self, pre_sum, l, r):
        if l == 0:
            return pre_sum[r]
        return pre_sum[r] - pre_sum[l-1]
