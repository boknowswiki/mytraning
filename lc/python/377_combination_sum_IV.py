#!/usr/bin/python -t

# array dp

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        memo = dict()
        
        def dfs(need):
            nonlocal n, nums, memo
            if need == 0:
                return 1
            
            if need in memo:
                #print(f"need {need}, memo need {memo[need]}")
                return memo[need]
            
            cnt = 0
            for i in range(n):
                if nums[i] <= need:
                    cnt += dfs(need-nums[i])

            memo[need] = cnt
            #print(f"add memo[need] {memo[need]}, need {need}")
            return cnt

        return dfs(target)

#Think about the recurrence relation first. How does the # of combinations of the target related to the # of combinations of numbers that are smaller than the target?
#So we know that target is the sum of numbers in the array. Imagine we only need one more number to reach target, this number can be any one in the array, right? So the # of combinations of target, comb[target] = sum(comb[target - nums[i]]), where 0 <= i < nums.length, and target >= nums[i].
#In the example given, we can actually find the # of combinations of 4 with the # of combinations of 3(4 - 1), 2(4- 2) and 1(4 - 3). As a result, comb[4] = comb[4-1] + comb[4-2] + comb[4-3] = comb[3] + comb[2] + comb[1].
#Then think about the base case. Since if the target is 0, there is only one way to get zero, which is using 0, we can set comb[0] = 1.
#EDIT: The problem says that target is a positive integer that makes me feel it's unclear to put it in the above way. Since target == 0 only happens when in the previous call, target = nums[i], we know that this is the only combination in this case, so we return 1.

#top down solution

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dfs(nums, dp, target):
            if dp[target] != -1:
                return dp[target]
            
            ret = 0
        
            n = len(nums)
            for i in range(n):
                if target >= nums[i]:
                    ret += dfs(nums, dp, target-nums[i])
            dp[target] = ret
            
            return ret
        
        dp = [-1] *(target+1)
        dp[0] = 1
        
        return dfs(nums, dp, target)

#bottom up solution

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] *(target+1)
        dp[0] = 1
        
        for i in range(1, len(dp)):
            for j in range(n):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]
                
        return dp[target]

#time limit exceeded

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 1
        
        ret = 0
        
        n = len(nums)
        for i in range(n):
            if target >= nums[i]:
                ret += self.combinationSum4(nums, target-nums[i])
                
        return ret

if __name__ =='__main__':
    s = [4,2,1]
    ss = Solution()
    print('answer is %d' % ss.combinationSum4(s, 32)) 
