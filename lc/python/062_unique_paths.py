#!/usr/bin/python -t

'''
#backtracking
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def bt(r, c, m, n):
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1

            return bt(r+1, c, m, n) + bt(r, c+1, m, n)

        return bt(0, 0, m, n)
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def bt(r, c, m, n, mymap):
            #print 'r=%d, c=%d, m=%d, n=%d, mymap %s' %(r,c,m,n,mymap)
            if r == m - 1 and c == n - 1:
                return 1
            if r >= m or c >= n:
                return 0

            if mymap[r+1][c] == -1:
                mymap[r+1][c] = bt(r+1, c, m, n, mymap)
            if mymap[r][c+1] == -1:
                mymap[r][c+1] = bt(r, c+1, m, n, mymap)

            return (mymap[r+1][c] + mymap[r][c+1])

        mymap = [-1]*(m+1)
        for i in range(m+1):
            mymap[i] = [-1]*(n+1)

        return bt(0, 0, m, n, mymap)


class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        cache = {}
        return self.findPath(m, n, cache)

    def findPath(self, m, n, cache):
        if (m, n) in cache:
            return cache[(m, n)]
        elif m == 1 or n == 1:
            return 1

        cache[(m, n)] = self.findPath(m - 1, n, cache) + self.findPath(m, n - 1, cache)

        return cache[(m, n)]



class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [0]*(m+1)
        for i in range(m+1):
            l[i] = [0]*(n+1)

        l[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                l[i][j] = l[i+1][j] + l[i][j+1]

        return l[0][0]



if __name__ =='__main__':
    s = Solution()
    #print('%d\n' % (s.uniquePaths(23, 12)))
    #print('%d\n' % (s.uniquePaths(3, 2)))
    print('%d\n' % (s.uniquePaths(7, 3)))

