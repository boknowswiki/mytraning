#!/usr/bin/python -t

def binarysearch(a, i):
    """
    e.g. a = [10, 20, 30, 40]
    print(Solution().bSearchNearest(a, 9)) <- 0
    print(Solution().bSearchNearest(a, 10)) <- 0
    print(Solution().bSearchNearest(a, 13)) <- 0
    print(Solution().bSearchNearest(a, 21)) <- 1
    print(Solution().bSearchNearest(a, 26)) <- 2
    print(Solution().bSearchNearest(a, 34)) <- 2
    print(Solution().bSearchNearest(a, 35)) <- 3
    print(Solution().bSearchNearest(a, 41)) <- 3
    """
    l = 0
    r = len(a) - 1

    while l < r:
        m = l + (r-l)/2
    
        print m, i
        if a[m] == i:
            return m
        elif a[m] < i:
            l = m + 1
        else:
            r = m

    if l > 0 and abs(i - a[l-1]) < abs(i - a[l]):
        return l-1
    return l
a = [10, 20, 30, 40]

print "%d\n" % binarysearch(a, 9)
print "%d\n" % binarysearch(a, 10)
print "%d\n" % binarysearch(a, 13)
print "%d\n" % binarysearch(a, 21)
print "%d\n" % binarysearch(a, 41)
