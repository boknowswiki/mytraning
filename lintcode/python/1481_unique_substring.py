class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: all unique substring
    """
    def uniqueSubstring(self, s, k):
        # Write your code here
        n = len(s)
        if n == 0 or n < k:
            return []

        ret = []
        v = set()

        for i in range(n-k+1):
            if s[i:i+k] not in v:
                v.add(s[i:i+k])
                ret.append(s[i:i+k])

        #print(sorted(ret))
        return sorted(ret)
                
