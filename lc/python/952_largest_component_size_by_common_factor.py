#!/usr/bin/python -t

#union find solution

class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def largestComponentSize(self, A):
        B = []
        for x in A:
            facs = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x /= d
                    facs.append(d)
                d += 1

            if x > 1 or not facs:
                facs.append(x)
            B.append(facs)

        primes = list({p for facs in B for p in facs})
        prime_to_index = {p: i for i, p in enumerate(primes)}

        dsu = DSU(len(primes))
        for facs in B:
            for x in facs:
                dsu.union(prime_to_index[facs[0]], prime_to_index[x])

        count = collections.Counter(dsu.find(prime_to_index[facs[0]]) for facs in B)
        return max(count.values())


# union find solution
# passed all the test cases but tle

import math
class uf:
    def __init__(self, N):
        self.p = range(N)
        self.sz = [1] * N
        self.max = 1

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            self.p[xr] = yr
            self.sz[yr] += self.sz[xr]
            self.max = max(self.max,self.sz[yr])

class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        myuf = uf(n)
        d = {}
        
        for i in range(n):
            a = A[i]
            j = 2
            while j*j <= a:
                if a%j == 0:
                    if j not in d:
                        d[j] = i
                    else:
                        myuf.union(i, d[j])
                    if a/j not in d:
                        d[a/j] = i
                    else:
                        myuf.union(i, d[a/j])
                j += 1
            if a not in d:
                d[a] = i
            else:
                myuf.union(i, d[a])
                
        return myuf.max


