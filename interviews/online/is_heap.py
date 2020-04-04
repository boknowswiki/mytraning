#!/usr/bin/python -t

import math
import os
import random
import re
import sys



# Complete the is_heap function below.
def is_heap(a):
    n = len(a)
    return helper(a, n-1, 1)

def helper(a, end, index):
    if index > (end-2)/2:
        return 1

    if a[index] <= a[index*2] and a[index] <= a[index*2+1] and helper(a, end, 2*index) and helper(a, end, 2*index+1):
        return 1
    return 0


a = [0, 1, 2, 3, 3, 4, 6, 3, 8]
a = [0, 3, 4, 2, 8]
print is_heap(a)
