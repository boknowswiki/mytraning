#!/usr/bin/python -t

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = len(str)
        sign = 1
        i = 0
        num = 0
        max_int = 2**31-1
        min_int = -2**31
        if n == 0:
            return 0
        while i < n and str[i] == ' ':
            i = i + 1        
        if i < n and str[i] == '-':
            sign = -1
            i = i + 1
        elif i < n and str[i] == '+':
            sign = 1
            i = i + 1

            
        while i < n and (str[i] >= '0' and str[i] <= '9'):
            s = ord(str[i]) - ord('0')
            if (num > (max_int/10)) or \
                (num == (max_int/10) and (ord(str[i]) - ord('0') >= 8)):
                if sign == -1:
                    return min_int
                else:
                    return max_int
            num = num * 10 + s
            i = i + 1
            
        return sign * num

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = len(str)
        if n == 0:
            return 0
        ret = 0
        sign = 1
        i = 0
        #skip the leading spaces
        while i < n and str[i] == ' ':
            i = i + 1

        if i == n:
            return 0
        
        if str[i] == '-':
            sign = -1
            i = i + 1
        elif str[i] == '+':
            sign = 1
            i = i + 1

        while i < n and (str[i] >= '0' and str[i] <= '9'):
            ret = ret * 10 + (ord(str[i]) - ord('0'))
            #print str[i], ret
            i = i + 1

        ret = ret * sign

        if ret >= 2**31:
            return 2**31-1
        elif ret <= -2**31:
            return -2**31
        else:
            return ret

if __name__ =='__main__':
    s = Solution()
    print('%d\n' % (s.myAtoi('   -42')))

