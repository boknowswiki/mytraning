# stack and greedy
# time O(n)
# space O(n)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st = []
        v = set()

        last_pos = {c:i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in v:
                while st and c < st[-1] and i < last_pos[st[-1]]:
                    v.remove(st.pop())
                
                v.add(c)
                st.append(c)

        return "".join(st)
        
