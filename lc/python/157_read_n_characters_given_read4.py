#!/usr/bin/python -t

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        pos = 0
        buff = [''] * 4
        eof = False

        while !eof and pos < n:
            r_b = read4(buff)
            if r_b < 4:
                eof = True

            byte = min(n-pos, r_b)
            for i in byte:
                buf[pos+i] = buff[i]

            pos = pos + byte

        return pos

