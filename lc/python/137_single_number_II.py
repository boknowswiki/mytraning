#!/usr/bin/python -t

# array, bit manipulations
# time O(n)
# space O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Loner. 
        loner = 0
        
        # Iterate over all bits
        for shift in range(32):
            bit_sum = 0
            
            # For this bit, iterate over all integers
            for num in nums:
                
                # Compute the bit of num, and add it to bit_sum
                bit_sum += (num >> shift) & 1
            
            # Compute the bit of loner and place it
            loner_bit = bit_sum % 3
            loner = loner | (loner_bit << shift)

        # Do not mistaken sign bit for MSB.
        if loner >= (1 << 31):
            loner = loner - (1 << 32)
        
        return loner

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #c = [0] * 32
        ret = 0
        n = len(nums)
        for i in xrange(32):
            c = 0
            for j in xrange(n):
                if ((nums[j] >> i) & 1):
                    c = c + 1
            ret |= ((c%3) << i)

            if ret >= 2**31:
                ret -= 2**32
        return ret



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        ret = 3*sum(s) - sum(nums)
        ret = ret / 2

        return ret



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        three = 0

        for i in nums:
            two |= one & i
            one ^= i
            three = one & two
            one &= ~three
            two &= ~three

        return one


