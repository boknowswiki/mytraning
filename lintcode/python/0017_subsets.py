#!/usr/bin/python3 -t

# time O(n*2^n)
# space O(n)
#时间复杂度：O(n×2^n)。一共 2^n2 个状态，每种状态需要 O(n) 的时间来构造子集。

#空间复杂度：O(n)。临时数组 t 的空间代价是 O(n)，递归时栈空间的代价为 O(n)。

from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]

        nums.sort()
        ret = []
        self.dfs(nums, 0, [], ret)

        return ret

    def dfs(self, nums, index, path, ret):
        if index == len(nums):
            ret.append(list(path))
            return

        path.append(nums[index])
        self.dfs(nums, index+1, path, ret)
        path.pop()
        self.dfs(nums, index+1, path, ret)




if __name__ == '__main__':
    s = Solution()
    a = [0]
    a = [1,2,3]
    print(s.subsets(a))

# bfs


from collections import deque

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        nums.sort()
        ret = []
            
        q = deque([[]])
        
        while len(q) > 0:
            path = q.popleft()
            ret.append(path)
            
            for i in range(len(nums)):
                if not path or path[-1] < nums[i]:
                    new_path = list(path)
                    new_path.append(nums[i])
                    q.append(new_path)
                    
        return ret
        
        
        

# dfs

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums.sort()
        
        ret = []
        
        self.dfs(nums, 0, [], ret)
        
        return ret
        
    def dfs(self, nums, start, path, ret):
        ret.append(list(path))

        
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i+1, path, ret)
            path.pop()
            
        return
    


class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums.sort()
        
        ret = []
        
        self.dfs(nums, 0, [], ret)
        
        return ret
        
    def dfs(self, nums, start, path, ret):
        #exit point
        if start == len(nums):
            ret.append(list(path))
            return

        # add nums[start]
        path.append(nums[start])
        self.dfs(nums, start+1, path, ret)
        
        # don't add nums[start]
        path.pop()
        self.dfs(nums, start+1, path, ret)
            
        return
    
