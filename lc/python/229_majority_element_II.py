#!/usr/bin/python -t

# hash map and sorting
# time O(n)
# space O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)

        return result

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        if len(nums) == 0:
            return ret
        
        cnt1 = cnt2 = 0
        val1, val2 = 0, 1
        
        for i in nums:
            if cnt1 == 0 and (val2 != i):
                cnt1 = cnt1 + 1
                val1 = i
            elif (cnt2 == 0) and (val1 != i):
                cnt2 = cnt2 + 1
                val2 = i
            elif val1 == i:
                cnt1 = cnt1 + 1
            elif val2 == i:
                cnt2 = cnt2 + 1
            else:
                cnt1 = cnt1 - 1
                cnt2 = cnt2 - 1
        #print val1, val2        
        if nums.count(val1) > (len(nums)//3):
            ret.append(val1)
        if (val1 != val2) and nums.count(val2) > (len(nums)//3):
            ret.append(val2)
            
        return ret
