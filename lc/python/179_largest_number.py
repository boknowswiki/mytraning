#!/usr/bin/python -t

#time O(nlogn) space O(n)

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
    
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        comp=lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        new_nums = map(str, nums)
        new_nums.sort(cmp=comp, reverse=True)
        ret = "".join(new_nums)
        return "0" if ret[0] == "0" else ret


def largestNumber(self, num):
    comp=lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
    num=map(str,num)
    num.sort(cmp=comp,reverse=True)
    return str(int("".join(num)))

#More explanation
#
#1-we define a function that compares two string (a,b) . we consider a bigger than b if a+b>b+a
#for example : (a="2",b="11") a is bigger than b because "211" >"112"
#
#2-convert all elements of the list from int to string
#
#3-sort the list descendingly using the comparing function we defined
#for example sorting this list ["2","11","13"] using the function defined in step 1 would produce ["2","13","11"]
#
#4-we concatatenate the list "21311"
