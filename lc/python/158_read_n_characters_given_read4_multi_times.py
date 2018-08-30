#!/usr/bin/python -t

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    def __init__(self):
        self.buff = [''] * 4
        self.offset = 0
        self.bufsize = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        pos = 0
        eof = False

        while !eof and pos < n:
            if self.bufsize == 0:
                self.bufsize = read4(self.buff)
                if self.bufsize < 4:
                    eof = True

            byte = min(n-pos, self.bufsize)
            for i in byte:
                buf[pos+i] = self.buff[self.offset + i]

            self.offset = (self.offset + byte) % 4
            self.bufsize = self.bufsize - byte
            pos = pos + byte

        return pos

