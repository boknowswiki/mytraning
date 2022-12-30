#!/usr/bin/python -t

# two pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        nums.sort()

        ret = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            need = -nums[i]
            while j < k:
                if nums[j]+nums[k] == need:
                    #found = [nums[i], nums[j], nums[k]]
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and j > i+1 and nums[j] == nums[j-1]: j += 1
                    while j < k and k < n-1 and nums[k] == nums[k+1]: k -= 1
                elif nums[j] + nums[k] < need:
                    j += 1
                else:
                    k -= 1

        return ret

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ret = []
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = n - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                
                if total == 0:
                    ret.append((nums[i], nums[start], nums[end]))
                    while start < end and nums[start] == nums[start+1]:
                        start = start + 1
                    while start < end and nums[end] == nums[end-1]:
                        end = end - 1
                    start = start + 1
                    end = end - 1
                elif total < 0:
                    start = start + 1
                else:
                    end = end - 1

                
        return ret
