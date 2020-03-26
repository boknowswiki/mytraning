#!/usr/bin/python -t


from __future__ import print_function

import os
import sys



# Complete the function below.

def convolve(a, k):
    n = len(a)
    m = len(k)
    ret = []

    for i in range(n-m+1):
        total = 0
        for j in range(m):
            val = a[i+j]*k[j]
            total += val
        ret.append(total)

    return ret
    
