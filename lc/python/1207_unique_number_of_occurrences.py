# hash map
# time O(n)
# space O(n)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if not arr:
            return True
        
        m = {}
        for a in arr:
            m[a] = m.get(a, 0) + 1
            
        s = set()
        for k, v in m.items():
            s.add(v)
        return len(s) == len(m)
