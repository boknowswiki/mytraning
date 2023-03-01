# sort
# merge sort
# time O(nlogn)
# space O(1)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums, 0, len(nums)-1)

    def mergesort(self, nums, start, end) -> List[int]:
        #print(f"start {start}, end {end}")
        if start == end:
            #print(f"nums start {start}, {nums[start]}")
            return [nums[start]]
        if start < end:
            mid = start + (end-start)//2

            left = self.mergesort(nums, start, mid)
            right = self.mergesort(nums, mid+1, end)

            #print(f"left {left}, right {right}")
            return self.merge(left, right)

        return []

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        ret = []
        l1_index = 0
        l2_index = 0

        while l1_index < len(l1) and l2_index < len(l2):
            if l1[l1_index] < l2[l2_index]:
                ret.append(l1[l1_index])
                l1_index += 1
            else:
                ret.append(l2[l2_index])
                l2_index += 1

        if l1_index < len(l1):
            ret.extend(l1[l1_index:])
        if l2_index < len(l2):
            ret.extend(l2[l2_index:])

        return ret



# quick sort
# time O(n^2) worst cast
# space O(1)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)

        return nums

    def quicksort(self, nums, start, end):
        if start < end:
            pivot = self.partition(nums, start, end)

            self.quicksort(nums, start, pivot-1)
            self.quicksort(nums, pivot+1, end)

        return

    def partition(self, nums, start, end):
        pivot = nums[end]
        index = start

        for i in range(start, end):
            if nums[i] <= pivot:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1

        nums[index], nums[end] = nums[end], nums[index]
        return index
