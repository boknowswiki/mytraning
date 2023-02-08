#!/usr/bin/python -t

# dp, greedy

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return False
        last_pos = 0
        i = 0

        while i < n and i <= last_pos:
            last_pos = max(last_pos, i + nums[i])
            i += 1

        return i == n

#time O(n) space O(1)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        lastpos = n - 1
        
        for i in range(n-1, -1, -1):
            if i + nums[i] >= lastpos:
                lastpos = i
                
        return lastpos == 0


#time limit exceeded
#time O(2^n) space O(2n)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = [0] *len(nums)
        m[len(nums)-1] = 1
        
        for i in range(len(nums)-2, -1, -1):
            further = min(i + nums[i], len(nums)-1)
            for j in range(i+1, further+1):
                if m[j] == 1:
                    m[i] = 1
                    break
                    
                
        return m[0] == 1


#memory limit exceeded
#time O(2^n) space O(2n)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums, start, m):
            if m[start] != 0:
                return True if m[start] == 1 else False
            
            further_index = min(start+nums[start], len(nums)-1)
            
            for index in range(start+1, further_index+1):
                if dfs(nums, index, m):
                    m[start] = 1
                    return True
            m[start] = -1
            return False
        
        m = [0] *len(nums)
        m[len(nums)-1] = 1
        return dfs(nums, 0, m)


#time or memory limit exceeded
#time O(2^n) space O(n)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums, start):
            if start == len(nums) -1:
                return True
            
            further_index = min(start+nums[start], len(nums)-1)
            
            for index in range(start+1, further_index+1):
                if dfs(nums, index):
                    return True
                
            return False
        
        return dfs(nums, 0)
