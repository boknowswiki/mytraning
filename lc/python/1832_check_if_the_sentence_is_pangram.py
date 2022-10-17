# string and hashmap
# time O(n)
# space O(n)

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for c in sentence:
            s.add(c)
            
        return len(s) == 26
