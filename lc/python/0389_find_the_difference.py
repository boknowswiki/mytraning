# hash map
# time O(n)
# space O(n)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t

        s_cnt = collections.Counter(s)
        t_cnt = collections.Counter(t)

        for k, v in t_cnt.items():
            if k not in s:
                return k
            if v == s_cnt[k]+1:
                return k

        return ""

# bit manipulation
# time O(n)
# space O(1)


    class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Initialize ch with 0, because 0 ^ X = X
        # 0 when XORed with any bit would not change the bits value.
        ch = 0

        # XOR all the characters of both s and t.
        for char_ in s:
            ch ^= ord(char_)

        for char_ in t:
            ch ^= ord(char_)

        # What is left after XORing everything is the difference.
        return chr(ch)
