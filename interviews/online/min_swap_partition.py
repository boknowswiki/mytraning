#!/usr/bin/python -t


def min_swap_partition(p, a):
    # Write your code here
    n = len(a)
    print p, a
    if n == 0:
        return 0
    index = 0
    while index < n and a[index] < p:
        index += 1

    if index == n:
        return 0
    cnt = 0
    for i in range(index+1, n):
        if a[i] < p:
            a[index], a[i] = a[i], a[index]
            index += 1
            cnt += 1
            while index < i and a[index] < p:
                index += 1


    return cnt

p = 5
a = [8, 1, 6, 0, 7, 3, 1, 6, 7, 5, 5, 3, 9, 2, 3, 4, 9, 9, 3, 6, 8, 0, 0, 9, 7, 4, 9, 2, 5, 0, 0, 4, 7, 5, 7, 2, 3, 2, 7, 3, 7, 0, 7, 7, 5, 0, 8, 8, 0, 6, 7, 6, 5, 6, 4, 7, 3, 5, 7, 0, 4, 3, 8, 5, 8, 4, 4, 5, 3, 4, 6, 5, 3, 4, 6, 0, 7, 4, 8, 6, 3, 0, 0, 7, 5, 7, 6, 3, 0, 2, 5, 1, 2, 1, 7, 0, 8, 0, 9, 7]

print min_swap_partition(p, a)
aa = sorted(a)
print aa[46]
print aa[47]
