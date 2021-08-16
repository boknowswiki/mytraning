#!/usr/bin/python -t

# heap

# 贪心+哈希表的做法
# 一个哈希表来建立字符和其出现次数之间的映射，然后需要一个堆来保存这每一堆映射，按照出现次数来排序。然后如果堆不为空我们就开始循环，我们找出k和str长度之间的较小值，然后从0遍历到这个较小值，对于每个遍历到的值，如果此时堆为空了，说明此位置没法填入字符了，返回空字符串，否则我们从堆顶取出一对映射，然后把字母加入结果res中，此时映射的个数减1，如果减1后的个数仍大于0，则我们将此映射加入临时集合v中，同时str的个数len减1，遍历完一次，我们把临时集合中的映射对由加入堆中


import heapq, collections

class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: a string such that the same characters are at least distance k from each other
    """
    def rearrangeString(self, s, k):
        # Write your code here
        l = [(-cnt, c) for (c, cnt) in collections.Counter(s).items()]
        heapq.heapify(l)
        ret = []
        tmp = []

        while len(ret) < len(s):
            while tmp:
                heapq.heappush(l, tmp.pop())
            for _ in range(max(k, 1)):
                if not l and tmp:
                    return ""
                if l:
                    cnt, c = heapq.heappop(l)
                    ret.append(c)
                    cnt += 1
                    if cnt < 0:
                        tmp.append((cnt, c))

        return "".join(ret)
