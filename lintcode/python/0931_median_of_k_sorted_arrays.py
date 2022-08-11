#!/usr/bin/python -t

# divid and conqure and binary search
# time O(klogmlogn) m is the min val to max val range in the nums
# space O(1)


from typing import (
    List,
)

import heapq

class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def find_median(self, nums: List[List[int]]) -> float:
        # write your code hereg
        if not nums:
            return 0.0

        n = sum(len(arr) for arr in nums)
        if n == 0:
            return 0.0

        if n % 2 == 1:
            return self.find_kth(nums, n // 2 + 1) * 1.0
        return (self.find_kth(nums, n // 2) + self.find_kth(nums, n // 2 + 1)) / 2.0

    # k is one-based, from 1 to n
    def find_kth(self, arrs, k):
        start, end = self.get_range(arrs)

        # find the first num that there are >= k nums <= num
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_smaller_or_equal(arrs, mid) >= k:
                end = mid
            else:
                start = mid
        if self.get_smaller_or_equal(arrs, start) >= k:
            return start
        return end

    def get_range(self, arrs):
        start = min(arr[0] for arr in arrs if len(arr))
        end = max(arr[-1] for arr in arrs if len(arr))
        return start, end

    def get_smaller_or_equal(self, arrs, val):
        count = 0
        for arr in arrs:
            count += self.get_smaller_or_equal_in_arr(arr, val)
        return count

    def get_smaller_or_equal_in_arr(self, arr, val):
        if not arr:
            return 0

        # find the first num > val
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] > val:
                end = mid
            else:
                start = mid

        if arr[start] > val:
            return start
        if arr[end] > val:
            return end
        return end + 1




# heap
# time O(klogn)
# space O(k)

from typing import (
    List,
)

import heapq

class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def find_median(self, nums: List[List[int]]) -> float:
        # write your code hereg
        n = len(nums)
        if n == 0:
            return 0

        cnt = self.get_total(nums)

        left, right = self.find_mid(nums, cnt)

        if cnt % 2 == 0:
            return (left + right) / 2.0
        else:
            return right / 1.0


    def get_total(self, nums):
        cnt = 0

        for num in nums:
            cnt += len(num)

        return cnt

    def find_mid(self, nums, cnt):
        left_index = cnt // 2
        right_index = cnt//2 + 1
        index = 0
        left, right = 0, 0

        hq = []

        for i in range(len(nums)):
            if nums[i]:
                heapq.heappush(hq, (nums[i][0], i, 0))

        while hq:
            val, row, col = heapq.heappop(hq)
            index += 1
            if index == left_index:
                left = val
            if index == right_index:
                right = val
                break

            if col+1 < len(nums[row]):
                heapq.heappush(hq, (nums[row][col+1], row, col+1))

        return left, right
