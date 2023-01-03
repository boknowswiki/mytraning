# string and matrix
# time O(m*n)
# space O(1)

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        if m == 0:
            return 0

        n = len(strs[0])
        if n == 0:
            return

        ret = 0

        for i in range(n):
            for j in range(1, m):
                if strs[j][i] < strs[j-1][i]:
                    ret += 1
                    break
        
        return ret
      
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        for i in zip(*strs):
            if list(i)!=sorted(i):
                c+=1
        return c
