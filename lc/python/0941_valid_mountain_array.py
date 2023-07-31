# array
# time O(n)
# space O(1)

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        index = 0

        while index + 1 < n and arr[index] < arr[index+1]:
            index += 1

        if index == 0 or index == n-1:
            return False

        while index+ 1 < n and arr[index] > arr[index+1]:
            index += 1

        return index == n-1
