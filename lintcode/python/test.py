#!/usr/bin/python -t

class quick_sort:
    def sort(self, l):
        n = len(l)

        self.quicksort(l, 0, n-1)

        return l

    def quicksort(self, l, start, end):
        if start > end:
            return

        part = self.partition(l, start, end)

        self.quicksort(l, start, part-1)
        self.quicksort(l, part+1, end)

    def partition(self, l, start, end):
        part = l[end]
        i = start

        for j in range(start, end):
            if l[j] <= part:
                l[i], l[j] = l[j], l[i]
                i += 1

        l[i], l[end] = l[end], l[i]
        
        return i


if __name__ == '__main__':
    l = [2, 2, 1, 1, 3, 5, 9, 1]
    ss = quick_sort()
    print "answer is \n"
    print ss.sort(l)


