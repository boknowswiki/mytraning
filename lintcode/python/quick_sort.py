#!/usr/bin/python -t

class quick_sort:
    def sort(self, l):
        n = len(l)
        self.quicksort(l, 0, n-1)
        return l

    def quicksort(self, l, low, high):
        if low < high:
            part = self.partition(l, low, high)
            self.quicksort(l, low, part-1)
            self.quicksort(l, part+1, high)

    def partition(self, l, low, high):
        pivot = l[high]

        #i = low-1
        i = low

        for j in range(low, high):
            if l[j] <= pivot:
                #i += 1
                l[i], l[j] = l[j], l[i]
                i += 1

        l[i], l[high] = l[high], l[i]

        return i

if __name__ == '__main__':
    l = [2, 2, 1, 1, 3, 5, 9, 1]
    ss = quick_sort()
    print "answer is \n"
    print ss.sort(l)


