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
        if n < 1:
            return []
            
        self.l = [[0] * (n) for _ in range(n)]
        self.ret = []
        for i in range(n):
            self.l[i][0] = A[i]
        print self.l
            
        #j = 1
        #while j < n:
        #    i = 0
        #    while i + (1<<j)-1 <= n:
        #        self.l[i][j] = min(self.l[i][j-1], self.l[i+(1<<(j-1))][j-1])
        #        i = i + 1
        #    j = 1<<j
        for j in range(1, n):
            for i in range(0, n):
                if i + (1<<j) -1 < n:
                    self.l[i][j] = min(self.l[i][j-1], self.l[i+(1<<(j-1))][j-1])

        #print self.l
            
        for q in queries:
            l, r = q
            #k = int(math.log(r-l+1)/math.log(2))
            k = int(math.log((r-l+1), 2))
            #print k
            ret = min(self.l[l][k], self.l[r-(1<<k)+1][k])
            self.ret.append(ret)

        return self.ret

if __name__ == '__main__':
    #s = [1,2,7,8,5]
    #q = [(1,2),(0,4),(2,4)]
    s = [10]
    q = [(0,0)]
    s = [100,99,98,97,96,95,94,93,92,91,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,90,89,88,87,86,85,84,83,82,81,71,72,73,74,75,76,77,78,79,80,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]
    q = [(0,99),(0,49),(0,99),(0,59),(0,39),(29,59)]
    ss = Solution()
    print "answer is %s" % ss.intervalMinNumber(s, q)

