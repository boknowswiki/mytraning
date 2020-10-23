#!/usr/bin/python -t

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: the smallest K for which A and B are K-similar
    """
    def kSimilarity(self, A, B):
        # Write your code here
        if A == B:
            return 0
        vis = set()
        from collections import deque
        queue = deque()
        vis.add(A)
        queue.append(A)
        res = 0
        while len(queue)!=0:
            res += 1
            size = len(queue)
            for i in range(size):
                s = queue.popleft()
                i = 0
                while (s[i] == B[i]):
                    i += 1
                for j in range(i + 1, len(A)):
                    if (s[j] == B[j] or s[i] != B[j]):
                        continue
                    ss = [c for c in s]
                    ss[i], ss[j] = s[j], s[i]
                    ss = "".join(ss)
                    if (ss == B):
                        return res
                    if ss not in vis:
                        vis.add(ss)
                        queue.append(ss)
        return res
