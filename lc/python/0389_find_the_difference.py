# hash map
# time O(n)
# space O(n)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t

        s_cnt = collections.Counter(s)
        t_cnt = collections.Counter(t)

        for k, v in t_cnt.items():
            if k not in s:
                return k
            if v == s_cnt[k]+1:
                return k

        return ""
