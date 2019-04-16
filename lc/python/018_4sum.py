#!/usr/bin/python -t

#this faster

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        ret = {}
        
        s_nums = sorted(nums)
        d = {}
        
        for i in range(n-3):
            for j in range(i+1, n-2):
                s = s_nums[i] + s_nums[j]
                try:
                    d[target-s].append([i, j])
                except KeyError:
                    d[target-s] = [[i, j]]
        for key, temp in d.items():
            for pair in temp:
                j = pair[1] + 1
                k = n - 1
                while j < k:
                    current = s_nums[j] + s_nums[k]
                    if current == key:
                        result = (s_nums[pair[0]], s_nums[pair[1]], s_nums[j], s_nums[k])
                        ret[result] = True
                        j += 1
                    elif current < key:
                        j += 1
                    else:
                        k -= 1
        return ret.keys()

