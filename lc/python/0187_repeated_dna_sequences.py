# hash map and string
# time O(n)
# space O(n)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s:
            return []

        n = len(s)
        d = dict()
        ret = []

        for i in range(n-9):
            sub_s = s[i:i+10]
            d[sub_s] = d.get(sub_s, 0)+1

        for k, v in d.items():
            if v > 1:
                ret.append(k)

        return ret
      
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)     
        seen, output = set(), set()

        # iterate over all sequences of length L
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output
