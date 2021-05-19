class Solution:
    """
    @param s: a string
    @return: return List[str]
    """
    def findRepeatedDnaSequences(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return 0

        d = {}
        ret = []

        for i in range(n-10+1):
            d[s[i:i+10]] = d.get(s[i:i+10], 0) + 1
        
        #print(d)
        for k, v in d.items():
            if v > 1:
                ret.append(k)

        return ret
