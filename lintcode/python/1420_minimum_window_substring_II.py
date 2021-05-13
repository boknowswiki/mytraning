class Solution:
    """
    @param S: A source string
    @param T: A target string
    @return: The String contains the smallest substring of all T letters.
    """
    def minWindowII(self, S, T):
        # Write your code here
        s = S+S
        ret = ""
        td = {}
        for k in T:
            td[k] = td.get(k, 0) + 1

        sd = {}
        tlen = len(td)
        match = 0
        min_len = sys.maxsize
        j = 0

        for i, v in enumerate(s):
            if v in td:
                sd[v] = sd.get(v, 0) + 1
                if sd[v] == td[v]:
                    match += 1
            while match == tlen:
                if i-j < min_len:
                    min_len = i-j
                    ret = s[j:i+1]

                if s[j] in sd:
                    if sd[s[j]] == td[s[j]]:
                        match -= 1
                    sd[s[j]] -= 1
                    if sd[s[j]] == 0:
                        del sd[s[j]]
                j += 1

        return ret

