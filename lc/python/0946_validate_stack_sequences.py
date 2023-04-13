# stack
# time O(n)
# space O(n)

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        pop_cnt = 0

        for val in pushed:
            st.append(val)
            while st and pop_cnt < len(popped) and st[-1] == popped[pop_cnt]:
                st.pop()
                pop_cnt += 1

        return pop_cnt == len(popped)
