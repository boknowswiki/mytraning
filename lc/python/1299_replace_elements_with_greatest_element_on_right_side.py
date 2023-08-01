# array
# time O(n)
# space O(1)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return arr
        if n == 1:
            arr[0] = -1
            return arr

        cur_max = arr[n-1]

        for i in range(n-2, -1, -1):
            cur = arr[i]
            arr[i] = cur_max
            cur_max = max(cur_max, cur)

        arr[-1] = -1

        return arr
