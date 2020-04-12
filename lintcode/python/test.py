#!/usr/bin/python -t

class sort():
    def __init__(self, l):
        self.l = l
    def mergesort(self):
        ll = self.helper(self.l, 0, len(self.l)-1)
        return ll
    def helper(self, l, start, end):
        if start == end:
            return [l[start]]

        mid = (start+end)/2

        l1 = self.helper(l, start, mid)
        l2 = self.helper(l, mid+1, end)

        return self.merge(l1, l2)

    def merge(self, l1, l2):
        n1 = len(l1)
        n2 = len(l2)
        i1 = i2 = 0
        ret = []
        while i1 < n1 and i2 < n2:
            if l1[i1] < l2[i2]:
                ret.append(l1[i1])
                i1 += 1 
            else:
                ret.append(l2[i2])
                i2 += 1

        if i1 < n1:
            ret.extend(l1[i1:])
        if i2 < n2:
            ret.extend(l2[i2:])

        return ret

if __name__ == "__main__":
    l = [3, 2, 2, 1, 4]
    s = sort(l)
    ss = s.mergesort()
    print l
    print ss
