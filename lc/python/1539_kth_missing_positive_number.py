# binary search

# time O(logn)
# space O(1)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k
    
    
# time O(logn)
# space O(1)

# Explanation
# Assume the final result is x,
# And there are m number not missing in the range of [1, x].
# Binary search the m in range [0, A.size()].

# If there are m number not missing,
# that is A[0], A[1] .. A[m-1],
# the number of missing under A[m] is A[m] - 1 - m.

# If A[m] - 1 - m < k, m is too small, we update left = m.
# If A[m] - 1 - m >= k, m is big enough, we update right = m.

# Note that, we exit the while loop, l = r,
# which equals to the number of missing number used.
# So the Kth positive number will be l + k.

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        while l < r:
            mid = l + (r-l)//2
            if arr[mid] - 1 - mid < k:
                l = mid+1
            else:
                r = mid
                
        return l + k
