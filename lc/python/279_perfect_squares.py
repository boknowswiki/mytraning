#!/usr/bin/python -t

# bfs
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        #print(f"lst {lst}, tocheck {toCheck}")
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    #print(f"x {x}, y {y}")
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp
            #print(f"toCheck {toCheck}")

        return cnt

# dp

#dp[n] indicates that the perfect squares count of the given n, and we have:
#dp[0] = 0 
#dp[1] = dp[0]+1 = 1
#dp[2] = dp[1]+1 = 2
#dp[3] = dp[2]+1 = 3
#dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 } 
#      = Min{ dp[3]+1, dp[0]+1 } 
#      = 1               
#dp[5] = Min{ dp[5-1*1]+1, dp[5-2*2]+1 } 
#      = Min{ dp[4]+1, dp[1]+1 } 
#      = 2
#                        .
#                        .
#                        .
#dp[13] = Min{ dp[13-1*1]+1, dp[13-2*2]+1, dp[13-3*3]+1 } 
#       = Min{ dp[12]+1, dp[9]+1, dp[4]+1 } 
#       = 2
#                        .
#                        .
#                        .
#dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            min_val = sys.maxint
            j = 1
            while j*j <= i:
                min_val = min(dp[i-j*j]+1, min_val)
                j = j + 1
                
            dp[i] = min_val
            
        return dp[n]


#static dp

class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
