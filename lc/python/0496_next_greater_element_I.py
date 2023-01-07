
# stack and hash map
# time O(n)
# space O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        d = dict()

        for num in nums2:
            while st and num > st[-1]:
                d[st.pop()] = num
            st.append(num)

        while not st:
            d[st.pop()] = -1

        ret = []
        for num in nums1:
            ret.append(d.get(num, -1))

        return ret
