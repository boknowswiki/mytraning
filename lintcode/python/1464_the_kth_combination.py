#!/usr/bin/python -t

# dfs


class Solution:
    """
    @param n: The integer n
    @param k: The integer k
    @return: Return the combination
    """
    def getCombination(self, n, k):
        # Write your code here
        ret = []
        self.index = 1
        nums = [i for i in range(1, n+1)]
        self.dfs(nums, k, [], 0, ret)

        return ret

    def dfs(self, nums, k, subset, startIndex, ret):
        if len(subset) == len(nums)//2:
            #print(subset)
            if self.index == k:
                #print(subset)
                ret.extend(subset)
            self.index+=1
            return
            
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, k, subset, i+1, ret)
            subset.pop()

        return

if __name__ == '__main__':
    s = Solution()
    a = 2
    b = 1
    print(s.getCombination(a, 1))