#!/usr/bin/python -t

# dp solution, jiyihua sousuo, time O(n^2) space O(n^2)

class Solution:
    """
    @param N: an integer
    @return: the probability that soup A will be empty first
    """
    def soupServings(self, N):
        # Write your code here
        if N >= 500:
            return 1.0
        
        self.memo = {}
        return self.dfs(N, N)
    
    def dfs(self, x, y):
        if (x, y) not in self.memo:
            if x <= 0 or y <= 0:
                    ans = 0.5 if x<=0 and y<=0 else 1.0 if x<=0 else 0.0
            else:
                ans = 0.25 * (self.dfs(x-100,y)+self.dfs(x-75,y-25)+\
                        self.dfs(x-50,y-50)+self.dfs(x-25,y-75))
            self.memo[x, y] = ans
            
        return self.memo[x,y]

