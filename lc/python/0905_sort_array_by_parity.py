# array
# time O(n)
# space O(1)

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        
        while l <= r:
            while l <= r and nums[l] % 2 == 0:
                l += 1

            while l <= r and nums[r] % 2 == 1:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums

  class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
