# binary search
# time O(nlogn)
# space O(1)

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        new_list = sorted([(intervals[i][0], i) for i in range(len(intervals))])
        #print(f"new list {new_list}")
        ret = []

        for inter in intervals:
            index = self.find_index(new_list, inter[1])
            #print(f"need {inter[1]}, get index {index}")
            ret.append(index)

        return ret

    def find_index(self, arr, target):
        l = 0
        r = len(arr)-1

        while l + 1 < r:
            mid = l + (r-l)//2
            if arr[mid][0] == target:
                return arr[mid][1]
            elif arr[mid][0] < target:
                l = mid
            else:
                r = mid

        if arr[l][0] >= target:
            return arr[l][1]
        if arr[r][0] >= target:
            return arr[r][1]

        return -1
