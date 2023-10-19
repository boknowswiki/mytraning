# string, stack
# time O(n)
# space O(n)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if not s:
            return not t

        if not t:
            return not s

        s_st = []
        t_st = []

        for c in s:
            if c != "#":
                s_st.append(c)
            else:
                if s_st:
                    s_st.pop()

        for c in t:
            if c != "#":
                t_st.append(c)
            else:
                if t_st:
                    t_st.pop()

        return s_st == t_st

# reverse

class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
