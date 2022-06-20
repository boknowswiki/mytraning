#!/usr/bin/python3 -t


# binary search
# time O(logn)
# space O(1)


class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        end = self.get_end(reader, target)

        start = 0

        while start + 1 < end:
            mid = start + (end-start)//2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start

        if reader.get(end) == target:
            return end

        return -1

    def get_end(self, reader, target):
        order = 1
        while reader.get(target*order) < target:
            order = order * 2

        return target*order

# binary search solution

"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index, 
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        r = 0
        while reader.get(r) < target:
            r = r*2 + 1
            
        l = 0
        while l < r:
            mid = (l+r)/2
            if reader.get(mid) < target:
                l = mid + 1
            else:
                r = mid
                
        if reader.get(l) == target:
            return l
        else:
            return -1

