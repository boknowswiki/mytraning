# array, two pointers
# time O(n)
# space O(1)

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dup_zeros = 0
        n = len(arr) - 1

        for left in range(n+1):
            if left > n-dup_zeros:
                break
            
            if arr[left] == 0:
                if left == n-dup_zeros:
                    arr[n] = 0
                    n -= 1
                    break
                dup_zeros += 1

        last = n - dup_zeros

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i+dup_zeros] = 0
                dup_zeros -= 1
                arr[i+dup_zeros] = 0
            else:
                arr[i+dup_zeros] = arr[i]

        return
