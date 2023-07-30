# array sort
# time O(n)
# space O(1)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        ret = [0] * n
        index = n-1

        while l <= r:
            l_val = nums[l]*nums[l]
            r_val = nums[r]*nums[r]
            if r_val >= l_val:
                ret[index] = r_val
                r -= 1
            else:
                ret[index] = l_val
                l += 1
            index -= 1

        return ret

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
