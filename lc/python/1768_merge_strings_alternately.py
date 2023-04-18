# string and two pointers
# time O(max(m,n))
# space O(1)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = []
        n = len(word1)
        m = len(word2)
        if n == 0:
            return word2
        if m == 0:
            return word1

        i, j = 0, 0
        idx = 0

        while i < n and j < m:
            if idx % 2 == 0:
                ret.append(word1[i])
                i += 1
            else:
                ret.append(word2[j])
                j += 1
            
            idx += 1

        if i == n:
            ret.extend(list(word2[j:]))
        if j == m:
            ret.extend(list(word1[i:]))

        return "".join(ret)
      
      
 class Solution(object):
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)
      
      
      
 class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        return "".join(result)
      
