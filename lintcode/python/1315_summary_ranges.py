#!/usr/bin/python -t

# array
# cover duplicated numbers

class Solution:
    """
    @param nums:  a sorted integer array without duplicates
    @return: the summary of its ranges
    """
    def summaryRanges(self, nums):
        # Write your code here
        un_dup_l = set(nums)
        un_dup_l = list(un_dup_l)
        un_dup_l.sort()
        #print un_dup_l
        
        # get length
        n = len(un_dup_l)
        # no element, return empty list
        if n == 0:
            return []
        
        # one element, return this value
        if n == 1:
            return [str(un_dup_l[0])]
        
                        
        ret = []
        
        # get start value
        start = str(un_dup_l[0])
        # get start index
        index = un_dup_l[0]
        
        # start from second one
        for i in range(1, n):
            prev = un_dup_l[i-1]
            # not the last element
            if i != n-1:
                # not continue
                #print un_dup_l[i], index
                if un_dup_l[i] != index+1:
                    if int(start) == index:
                        ret.append(start)
                        #print un_dup_l[i], start, index
                    else:
                        tmp = start + "->" + str(index)
                        ret.append(tmp)
                    start = str(un_dup_l[i])
                    index = un_dup_l[i]
                else:
                    index += 1
            else:
                #print index
                if un_dup_l[i] != index+1:
                    if int(start) != index:
                        tmp = start + "->" + str(index)
                        ret.append(tmp)
                        ret.append(str(un_dup_l[i]))
                    else:
                        ret.append(start)
                        ret.append(str(un_dup_l[i]))
                else:
                    tmp = start + "->" + str(un_dup_l[i])
                    ret.append(tmp)
        return ret
        
        

if __name__ == '__main__':
    ss = [0, 5, 9]
    print "input %s" % ss
    s = interview()
    print "answer is "
    print s.combin(ss)

