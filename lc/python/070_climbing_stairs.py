#!/usr/bin/python -t

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__ =='__main__':
    s = Solution()
    print('%s\n' % (s.climbStairs(35)))
    print('%s\n' % (s.climbStairs(1)))
    print('%s\n' % (s.climbStairs(2)))
    print('%s\n' % (s.climbStairs(3)))


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.mem = [0] * n
        def f(n):
            if n <= 0:
                return 1
            if n == 1:
                return 1
            if n == 2:
                return 2
            if self.mem[n] != 0:
                return self.mem[n]
            self.mem[n] = f(n-1) + f(n-2)
            return self.mem[n]
        return f(n-1)+f(n-2)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        l = [0]*(n)
        l[0] = 1
        l[1] = 2

        for i in xrange(2, n):
            l[i] = l[i-1] + l[i-2]

        return l[n-1]


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        l = [0]*(n+1)
        l[1] = 1
        l[2] = 2

        for i in xrange(3, n+1):
            l[i] = l[i-1] + l[i-2]

        return l[n]

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        first = 1
        second = 2

        for i in xrange(3, n+1):
            third = first + second
            first = second
            second = third

        return second

