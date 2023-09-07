# stack, array


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""

        ret = []
        st = []

        for c in s:
            if c == ")" and not st:
                continue
            ret.append(c)
            if c == "(":
                st.append((len(ret)-1, c))
            if c == ")" and st:
                st.pop()

        while st:
            del ret[st.pop()[0]]

        return "".join(ret)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)
