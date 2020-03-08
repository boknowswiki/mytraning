#!/usr/bin/python -t

class Solution:
    def sort(self, s):
        n = len(s)
        tmp = [0] * n
        s = self.merge_sort(s, 0, n-1, tmp)
        return s

    def merge_sort(self, s, start, end, tmp):
        if start < end:
            mid = (start+end)/2

            l1 = self.merge_sort(s, start, mid, tmp)
            l2 = self.merge_sort(s, mid+1, end, tmp)
            self.merge(s, start, mid, end, tmp)

        return tmp

    def merge(self, s, start, mid, end, tmp):
        i = start
        j = mid+1
        k = start

        while i <= mid and j <= end:
            if s[i] < s[j]:
                tmp[k] = s[i]
                i += 1
            else:
                tmp[k] = s[j]
                j += 1

            k += 1


        while i <= mid:
            tmp[k] = s[i]
            i += 1
            k += 1
        while j <= end:
            tmp[k] = s[j]
            j += 1 
            k += 1

        for i in range(start, end+1):
            s[i] = tmp[i]

        return


if __name__ == '__main__':
    s = [1,1,2,2, 9, 8, 4, 5, 3]
    ss = Solution()
    print "answer is\n"
    print ss.sort(s)

