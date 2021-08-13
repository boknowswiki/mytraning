#!/usr/bin/python -t

# heap

# 一个简单的写法。heap只需要对已经加入的gas排序，即可，所以不需要写comparator。
# 然后，对于这个题目的test cases，distance其实已经是拍好序的，所以2元组排序也可以省略。
# 剩下的就是核心的贪心code，比较简短容易理解。
# 
# 复杂度分析有点笨，欢迎流言指教:
# 
# 所有的元素都加入到heap，平摊复杂度O(n)，然后只需要弹出一个元素O(1)即可，整体是O(n)。
# 所有元素依次加入到heap，然后依次弹出，heap大小为1，所以整体是O(n)。
# 中间情况，平均有k个元素在heap中，建立堆为O(k)，最多加入弹出(n - k)次，总体为O(k + (n-k)logk) ~ O((n-k)logk)，如果k ~ n/2，最坏还是O(nlogn)。
# 

import heapq

class Solution:
    """
    @param target: The target distance
    @param original: The original gas
    @param distance: The distance array
    @param apply: The apply array
    @return: Return the minimum times
    """
    def getTimes(self, target, original, distance, apply):
        # Write your code here
        ret = 0
        index = 0
        max_hq = []

        while original < target:
            while distance[index] <= original:
                heapq.heappush(max_hq, apply[index])
                index += 1

            if len(max_hq) == 0:
                break

            original += heapq.heappop(max_hq)
            ret += 1

        if original >= target:
            return ret

        return -1
