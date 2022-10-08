
# merge sort
# time O(nlogn)
# space O(n)

# The smaller numbers on the right of a number are exactly those that merged from its right to its left during a stable sort. So I do mergesort with added tracking of those right-to-left merged.

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            #print(f"enum {enum}")
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                #print(f"enum {enum}, left {left}, right {right}")
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()

            #print(f"return enum {enum}")
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


# binary search and sort with Time Limit Exceeded
# time O(nlogn)
# space O(n)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_map = sorted((nums[i], i) for i in range(len(nums)))
        #print(sorted_map)
        ret = []

        for i in range(len(nums)):
            cnt = self.find(sorted_map, nums[i], i)
            ret.append(cnt)

        return ret
    def find(self, sorted_map, target, index):
        l = 0
        r = len(sorted_map)-1
        cnt = 0

        #print(f"target {target}, index {index}")
        while l + 1 < r:
            mid = l + (r-l)//2
            if sorted_map[mid][0] >= target:
                r = mid
            else:
                l = mid

        #print(f"l {l}, r {r}")
        if sorted_map[r][0] < target:
            for i in range(r+1):
                if sorted_map[i][1] > index:
                    cnt += 1

            #print(f"r cnt {cnt}")
            return cnt
        if sorted_map[l][0] < target:
            for i in range(l+1):
                if sorted_map[i][1] > index:
                    cnt += 1

            #print(f"l cnt {cnt}")
            return cnt

        return cnt
