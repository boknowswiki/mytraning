# dfs

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        set_list = set(words)
        ret = []

        def dfs(word):
            nonlocal set_list

            for i in range(1, len(word)):
                l = word[:i]
                r = word[i:]
                if l in set_list:
                    if r in set_list or dfs(r):
                        return True

            return False

        for w in words:
            if dfs(w):
                ret.append(w)

        return ret
