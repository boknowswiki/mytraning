# hash table
# time O(n)
# space O(n)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_set = set()
        ret = 0

        for j in jewels:
            j_set.add(j)
        
        for s in stones:
            if s in j_set:
                ret += 1

        return ret
