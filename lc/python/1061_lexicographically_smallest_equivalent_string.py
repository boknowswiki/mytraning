# union find

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = dict()

        def find(x):
            uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])

            return uf[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a > root_b:
                uf[root_a] = root_b
            else:
                uf[root_b] = root_a

        for i in range(len(s1)):
            union(s1[i], s2[i])

        ret = []

        for c in baseStr:
            ret.append(find(c))

        return "".join(ret)
