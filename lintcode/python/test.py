#!/usr/bin/python -t

class sort():
    def mergesort(self, l):
        if len(l) > 1:
            mid = len(l)/2

            left = l[:mid]
            right = l[mid:]

            self.mergesort(left)
            self.mergesort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    l[k] = left[i]
                    i += 1 
                else:
                    l[k] = right[j]
                    j += 1
                k += 1

            if i < len(left):
                l[k] = left[i]
                k += 1
                i += 1
            if j < len(right):
                l[k] = right[j]
                k += 1
                j += 1

        return


if __name__ == "__main__":
    l = [3, 2, 2, 1, 4]
    print l
    s = sort()
    s.mergesort(l)
    print l
