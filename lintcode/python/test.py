#!/usr/bin/python -t

class sort():
    def quicksort(self, l):
        self.helper(l, 0, len(l)-1)

        return

    def helper(self, l, start, end):
        if start < end:
            part = self.partition(l, start, end)
            self.helper(l, start, part-1)
            self.helper(l, part+1, end)

        return

    def partition(self, l, start, end):
        part = l[end]
        i = start

        while start < end:
            if l[start] <= part:
                l[i], l[start] = l[start], l[i]
                i += 1

            start += 1

        l[i], l[end] = l[end], l[i]

        return i


if __name__ == "__main__":
    l = [3, 2, 2, 1, 4]
    print l
    s = sort()
    s.quicksort(l)
    print l
