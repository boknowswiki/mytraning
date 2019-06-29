#!/usr/bin/python -t

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import math
class Solution:
    """
    @param A: An integer array
    @param queries: An query list
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        # write your code here
        n = len(A)
        if n <= 1:
            return []
            
        self.l = [[0] * (n+1) for _ in range(n+1)]
        self.ret = []
        for i in range(n):
            self.l[i][0] = A[i]
            
        j = 1
        while j < n:
            i = 0
            while i + 1<<j-1 <= n:
                self.l[i][j] = min(self.l[i][j-1], self.l[i+(1<<(j-1))][j-1])
                i = i + 1
            j = 1<<j
            
        for q in queries:
            l, r = q
            #k = int(math.log(r-l+1)/math.log(2))
            k = int(math.log((r-l+1), 2))
            print k
            ret = min(self.l[l][k], self.l[r-(1<<k)+1][k])
            self.ret.append(ret)

        return self.ret

if __name__ == '__main__':
    s = [1,2,7,8,5]
    q = [(1,2),(0,4),(2,4)]
    ss = Solution()
    print "answer is %s" % ss.intervalMinNumber(s, q)

