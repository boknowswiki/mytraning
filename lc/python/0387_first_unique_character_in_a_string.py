# hash map
# time O(n)
# space O(n)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        d = collections.defaultdict(list)

        for i in range(len(s)):
            d[s[i]].append(i)

        ret = len(s)

        for k, v in d.items():
            if len(v) == 1:
                ret = min(ret, v[0])

        return ret if ret != len(s) else -1
      
 class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
