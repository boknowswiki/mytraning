#!/usr/bin/python3 -t

# dfs
# time O(n^(target/min)), n is the conut of numbers, min is the minimal value.
# space O(n^(target/min))

from typing import (
    List,
)

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
             we will sort your return value in output
    """
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        # write your code here

        ret = []
        if not candidates:
            return ret

        c = sorted(set(candidates))

        self.dfs(c, 0, target, [], ret)

        return ret
    
    def dfs(self, c, start, target, path, ret):
        if target < 0:
            return

        if target == 0:
            ret.append(list(path))

        for i in range(start, len(c)):
            path.append(c[i])
            self.dfs(c, i, target-c[i], path, ret)
            path.pop()

        return

if __name__ == '__main__':
    s = Solution()
    a = [2, 3, 6, 7]
    b = 7
    print(s.combination_sum(a, b))


# dfs, better
# 时间复杂度
# 答案个数不知道, 假设为S;
# 每个答案用的时间=target;
# 所以总的时间复杂度= O(S*target), 是个NP问题

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        s = sorted(set(candidates))
        
        ret = []
        
        self.dfs(s, target, 0, [], ret)
        
        return ret
        
    def dfs(self, s, target, start, path, ret):
        if target == 0:
            ret.append(list(path))
            return
        
        for i in range(start, len(s)):
            if target < s[i]:
                return
            path.append(s[i])
            self.dfs(s, target-s[i], i, path, ret)
            path.pop()
            
        return
    

# DFS, better

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        c = sorted(set(candidates))
        ret = []
        self.dfs(c, target, 0, [], ret)
        
        return ret
        
    def dfs(self, c, target, start, combination, ret):
        if target < 0:
            return
        
        if target == 0:
            ret.append(list(combination))
            
        for i in range(start, len(c)):
            if target < c[i]:
                break
            combination.append(c[i])
            self.dfs(c, target-c[i], i, combination, ret)
            combination.pop()
            
        return
    
    

# DFS

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        c = sorted(set(candidates))
        ret = []
        self.dfs(c, target, 0, [], ret)
        
        return ret
        
    def dfs(self, c, target, start, combination, ret):
        if target < 0:
            return
        
        if target == 0:
            ret.append(list(combination))
            
        for i in range(start, len(c)):
            combination.append(c[i])
            self.dfs(c, target-c[i], i, combination, ret)
            combination.pop()
            
        return
    
    
