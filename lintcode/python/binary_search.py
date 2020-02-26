#!/usr/bin/python -t

def lower(s, l, r):
    while l +1 < r:
        mid = l + (r-l)/2
        if s[mid] < target:
            l = mid
        else:
            r = mid - 1

    if s[l] == target:
        return l
   
    if s[r] == target:
        return r

    return -1


def upper(s, l, r):
    while l +1 < r:
        mid = l + (r-l)/2
        if s[mid] > target:
            r = mid
        else:
            l = mid+1

    if s[r] == target:
        return r
   
    if s[l] == target:
        return l

    return -1
