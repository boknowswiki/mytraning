#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res

    def helpler(self, l, r, item, res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > 0:
            self.helpler(l, r - 1, item + ')', res)

# dfs, should work but hit time limit exceeded.
# and remove the step loop, it resovles the time limit exceeded issue. answer is below this

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        ret = []
        self.dfs(n, 0, 0, 0, "", ret)
        return ret
    
    def dfs(self, n, step, start, end, path, ret):
        if start > n or end > n or end > start:
            return

        if start == end == n:
            ret.append(path)
            return
        
        for i in range(step, 2*n):
            new_path = path + "("
            self.dfs(n, i+1, start+1, end, new_path, ret)
            new_path = path + ")"
            self.dfs(n, i+1, start, end+1, new_path, ret)

        return


# fix time limit exceeded

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        ret = []
        self.dfs(n, 0, 0, "", ret)
        return ret
    
    def dfs(self, n, start, end, path, ret):
        if start > n or end > n or end > start or start+end > 2*n:
            return

        if start == end == n:
            ret.append(path)
            return
        
        if start < n:
            new_path = path + "("
            self.dfs(n, start+1, end, new_path, ret)
        if end < start:
            new_path = path + ")"
            self.dfs(n, start, end+1, new_path, ret)

        return
