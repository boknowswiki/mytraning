#!/usr/bin/python -t

class quick_select:
    def sort(self, l, k):
        n = len(l)

        ret = self.quickselect(l, 0, n-1, k)

        return ret

    def quickselect(self, l, start, end, k):
        if start == end:
            return l[start]

        if k > 0 and k <= end:
            index = self.partition(l, start, end)

            if index == k:
                return l[index]

            if index > k:
                return self.quickselect(l, start, index-1, k)

            return self.quickselect(l, index+1, end, k-index)


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
    print l
    ss = quick_select()
    print "answer is \n"
    for i in range(len(l)):
        print ss.sort(l, i)

