#!/usr/bin/python -t

# heap


# 对每一组的quality和wage计算时薪，按照时薪排序。
# 对于合法的k个数，为了满足条件，每个人的工资都大于初始工资，且成比例，所以每个人的时薪一定是这k个人中最高的那个人的时薪（否则最高的人不满足初始工资）。
# 所以对每个人的时薪找k个quality和最小的且时薪低于这个人的即可。
# 利用优先队列即可完成上述操作。

import heapq

class Solution:
    """
    @param quality: an array
    @param wage: an array
    @param K: an integer
    @return: the least amount of money needed to form a paid group
    """
    def mincostToHireWorkers(self, quality, wage, K):
        # Write your code here
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K: qsum += heapq.heappop(heap)
            if len(heap) == K: res = min(res, qsum * r)
        return res


# Python, sort by wage quality ratio, then maintain k workers by removing the largest quality worker.
# 可以刪掉quality最大的人的原因是，題目的條件一。選中的k個人裡面，每個人要支付的ratio是一樣的（最大的那個ratio），所以這k個人誰quality多就代表我要多quality的錢。踢掉quality最多的人來減少我的支出。Loop從小ratio到大ratio，記錄每個進來和離開的人的quality。
