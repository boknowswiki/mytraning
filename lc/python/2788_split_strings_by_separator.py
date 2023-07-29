# string
# time O(n)
# space O(1)

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ret = []
        
        for w in words:
            l = w.split(separator)
            
            for ll in l:
                if len(ll) == 0:
                    continue
                ret.append(ll)
            
        return ret

  class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ret = []
        
        for w in words:
            tmp = ""
            for c in w:
                if c == separator and tmp != "":
                    ret.append(tmp)
                    tmp = ""
                if c != separator:
                    tmp += c
            if tmp != "":
                ret.append(tmp)

        return ret
