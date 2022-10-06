# binary search
# time O(log(m+n))
# space O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.find_kth(nums1, nums2, l//2)
        else:
            return (self.find_kth(nums1, nums2, l//2) + self.find_kth(nums1, nums2, l//2-1))/2
                    
    def find_kth(self, nums1, nums2, index):
        if not nums1:
            return nums2[index]
        if not nums2:
            return nums1[index]
        
        half_nums1, half_nums2 = len(nums1)//2, len(nums2)//2
        mid_nums1, mid_nums2 = nums1[half_nums1], nums2[half_nums2]
        if half_nums1 + half_nums2 < index:
            if mid_nums1 > mid_nums2:
                return self.find_kth(nums1, nums2[half_nums2+1:], index-half_nums2-1)
            else:
                return self.find_kth(nums1[half_nums1+1:], nums2, index-half_nums1-1)
        else:
            if mid_nums1 > mid_nums2:
                return self.find_kth(nums1[:half_nums1], nums2, index)
            else:
                return self.find_kth(nums1, nums2[:half_nums2], index)
            
   
  # reference the code blow
  def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
    
def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2 , len(b) // 2
    ma, mb = a[ia], b[ib]
    
    # when k is bigger than the sum of a and b's median indices 
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)
