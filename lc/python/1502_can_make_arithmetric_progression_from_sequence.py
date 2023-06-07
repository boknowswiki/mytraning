# sort, array

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 2:
            return False

        arr.sort()

        diff = arr[1] - arr[0]

        for i in range(1, n):
            if arr[i] - arr[i-1] != diff:
                return False

        return True
