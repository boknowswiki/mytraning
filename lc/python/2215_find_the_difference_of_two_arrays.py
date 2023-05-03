# hash table
# time O(n)
# space O(n)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1_set = set(nums1)
        n2_set = set(nums2)
        ret = [[], []]

        for i in n1_set:
            if i not in n2_set:
                ret[0].append(i)

        for i in n2_set:
            if i not in n1_set:
                ret[1].append(i)

        return ret
      
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1_set = set(nums1)
        n2_set = set(nums2)
        
        ret = []

        ret.append(list(n1_set-n2_set))
        ret.append(list(n2_set-n1_set))

        return ret
