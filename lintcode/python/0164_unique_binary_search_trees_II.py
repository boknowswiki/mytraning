#!/usr/bin/python -t

# dp solution

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        # state: dp[i][j], all unique BSTs in [i,j]
        # function: dp[i][j] = dp[i][j-1] + dp[j+1][n] and append tis to result
        # init: dp[0][0] = [None]
        # result: dp[1][n]
        
        if n == 0:
            return [None]
            
        dp = [[[None] for i in range(n+2)] for j in range(n+2)]
        
        for k in range(n):
            for i in range(n-k+1):
                dp[i][i+k] = []
                for root in range(i, i+k+1):
                    for left in dp[i][root-1]:
                        for right in dp[root+1][i+k]:
                            rootnode = TreeNode(root)
                            rootnode.left = left
                            rootnode.right = right
                            dp[i][i+k].append(rootnode)
                            
        return dp[1][n]


# dfs and divid and conquer

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        return self.dfs(1, n)
        
    def dfs(self, start, end):
        if start > end:
            return [None]
        ret = []
        
        for val in range(start, end+1):
            left = self.dfs(start, val-1)
            right = self.dfs(val+1, end)
            for l in left:
                for r in right:
                    root = TreeNode(val)
                    root.left = l
                    root.right = r
                    ret.append(root)
                    
        return ret

