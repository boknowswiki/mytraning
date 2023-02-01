# math hash map
# time O(n)
# space O(n)

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points: return True
        min_p=min([i[0] for i in points])
        max_p=max([i[0] for i in points])
        d=set()
        for i in points:
            d.add(tuple(i))
        for i in points:
            if (min_p+max_p-i[0], i[1]) not in d:
                return False
        return True
