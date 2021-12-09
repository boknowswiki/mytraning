#!/usr/bin/python -t

# bfs or dfs

import collections

class Solution:
    """
    @param D: The sorted set of digits.
    @param N: 
    @return: The number of positive integers that can be written.
    """
    def atMostNGivenDigitSet(self, D, N):
        # Write your code here
        q = collections.deque()
        # convert string to int
        D = [ord(c)-ord("0") for c in D]
        for x in D:
            if x <= N:
                q.append(x)
        cnt = 0
        while q:
            num = q.popleft()
            #print("pop",num)
            cnt += 1
            #print("D: ", D)
            for x in D:
                #print("x is", x)
                numX = num*10+x
                #print("get: ",numX)
                if numX <= N:
                    q.append(numX)

        return cnt



if __name__ == '__main__':
    s = Solution()
    a = ["1","3","5","7"]
    b = 100
    print(s.atMostNGivenDigitSet(a, b))