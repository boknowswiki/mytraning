#!/usr/bin/python -t

class Solution:
    """
    @param ids: ID number of items
    @param m: The largest number of items that can be remove
    @return: the result of the min item
    """
    def minItem(self, ids, m):
        # write your code here1
        num_counts = {}
        for id in ids:
            num_counts[id] = num_counts.get(id, 0) + 1

        counts = sorted(num_counts[id] for id in num_counts)[::-1]

        while counts and counts[-1] <= m:
            m -= counts.pop()

        return len(counts)
