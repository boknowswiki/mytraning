# array
# time O(n)
# space O(1)

class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True

        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing
      
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def helper(increase):
            nonlocal nums
            for i in range(1, len(nums)):
                if increase and nums[i] >= nums[i-1]:
                    continue
                elif not increase and nums[i-1] >= nums[i]:
                    continue

                return False

            return True


        return helper(True) or helper(False)
        
