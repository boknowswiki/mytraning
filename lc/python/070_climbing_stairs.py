#!/usr/bin/python -t

# dp
# time O(n)
# space O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] is the ways at ith step
        # dp[i] = dp[i-1] + dp[i-2]
        # dp[0] = 1, dp[1] = 1, dp[2] = 2
        # dp[n]
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

#time O(n) space O(1)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        first = 1
        second = 1
        
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
            
        return third

#time O(n) space O(n)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [0] * (n+1)
        l[0] = 1
        l[1] = 1
        
        for i in range(2, n+1):
            l[i] = l[i-1] + l[i-2]
            
        return l[n]

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        for i in range(2,n+1):
            tmp = b
            b = a + b
            a = tmp
            
        return b

class Solution(object):
    def __init__(self):
        self.d = {1:1, 2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dp(n):
            if n not in self.d:
                self.d[n] = dp(n-1) + dp(n-2)
            return self.d[n]
        
        return dp(n)

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

