# hash map, string
# time O(mn)
# space O(1)

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, c in enumerate(order):
            d[c] = i

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if d[words[i][j]] > d[words[i+1][j]]:
                        return False

                    break

        return True
