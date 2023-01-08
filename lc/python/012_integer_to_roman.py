#!/usr/bin/python -t

# hash map
# time O(1)
# space O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        value = [1000, 900, 500, 400, 
                    100, 90, 50, 40, 
                    10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD',
                    'C', 'XC', 'L', 'XL', 
                    'X', 'IX', 'V', 'IV', 'I']

        i = 0
        ret = ''
        while num > 0:
            n = num // value[i]
            for j in range(n):
                ret = ret + symbols[i]
                num = num - value[i]
            i = i + 1

        return ret

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        value = [1000, 900, 500, 400, 
                    100, 90, 50, 40, 
                    10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD',
                    'C', 'XC', 'L', 'XL', 
                    'X', 'IX', 'V', 'IV', 'I']

        i = 0
        ret = ''
        while num > 0:
            n = num / value[i]
            for j in xrange(n):
                ret = ret + symbols[i]
                num = num - value[i]
            i = i + 1

        return ret


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret_str =""
        left = num
        roms_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roms = {5: "V", 1: "I", 10:"X", 50: "L", 100: "C", 500:"D", 1000: "M", 4:"IV", 9:"IX", 90:"XC", 400:"CD", 900:"CM", 40:"XL"}
        #4, 9, 40, 90, 400, 900
        while left>0: # keep looping till you have represented the entire number
            for k in roms_list:
                if left>=k: # pick the best fit for representing the number
                    ret_str+=roms[k]
                    #print ret_str
                    left = left - k
                    break
                
        return ret_str



