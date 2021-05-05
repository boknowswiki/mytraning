class Solution:
    """
    @param startString: a string
    @param endString: a string
    @return: if startString can be converted to endString
    """
    def canTransfer(self, startString, endString):
        # write your code here
        if len(startString) != len(endString):
            return False
        dic = {}
        for s, e in zip(startString, endString):
            if s not in dic:
                dic[s] = e
            else:
                if dic[s] != e:
                    return False
        for v in dic.values():
            visited = set()
            while v in dic:
                visited.add(v)
                last = v
                v = dic[v]
                if v == last:
                    break
                if v in visited:
                    return False
        return True
