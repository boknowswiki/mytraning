#!/usr/bin/python3 -t


# time O(n*2^n)
# space O(n)

from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]

        nums.sort()
        ret = []
        self.dfs(nums, 0, [], ret)

        return ret

    def dfs(self, nums, index, path, ret):
        ret.append(list(path))

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i+1, path, ret)
            path.pop()

        
if __name__ == '__main__':
    s = Solution()
    a = [0]
    a = [1,2,3]
    print(s.subsets_with_dup(a))

# dfs

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        ret = []
        nums.sort()
        
        self.dfs(nums, 0, [], ret)
        
        return ret
        
    def dfs(self, nums, index, path, ret):
        ret.append(list(path))
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i+1, path, ret)
            path.pop()
            
        return
    
    
