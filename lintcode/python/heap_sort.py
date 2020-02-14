#!/usr/bin/python -t

class heap_sort:
    def sort(self, l):
        n = len(l)
        for i in range(n, -1, -1):
            self.heapify(l, n, i)

        for i in range(n-1, 0, -1):
            l[i], l[0] = l[0], l[i]
            self.heapify(l, i, 0)

        return l

    def heapify(self, l, end, start):
            largest = start
            left = 2*start + 1
            right = 2*start + 2

            if left < end and l[start] < l[left]:
                largest = left
            if right < end and l[largest] < l[right]:
                largest = right

            if largest != start:
                l[largest], l[start] = l[start], l[largest]

                self.heapify(l, end, largest)

if __name__ == '__main__':
    l = [4, 10, 3, 5, 1]
    ss = heap_sort()
    print "answer is \n"
    print ss.sort(l)


