# array string
# time O(n)
# space O(n)

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        for w in word1:
            w1 += w
            
        w2 = ""
        for w in word2:
            w2 += w
            
        return w1 == w2
