#heap


import heapq

class node:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y


class Solution:
    """
    @param arr: an array of integers
    @param k: an integer
    @return: the Kth smallest element in a specific array
    """
    def kthSmallest(self, arr, k):
        # write your code here
        hq = []
        m = len(arr)
        if k == 1:
            return arr[0][0]

        for i in range(m):
            if len(arr[i]) > 0:
                heapq.heappush(hq, (arr[i][0], i, 0))

        for i in range(k-1):
            val, x, y = heapq.heappop(hq)
            if y+1 < len(arr[x]):
                heapq.heappush(hq, (arr[x][y+1], x, y+1))

        ret, _, _ = heapq.heappop(hq)

        return ret
