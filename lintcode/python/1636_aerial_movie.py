#!/usr/bin/python -t

# binary search

class Solution:
    """
    @param t: the length of the flight
    @param dur: the length of movies 
    @return: output the lengths of two movies
    """
    def aerial_Movie(self, t, dur):
        # Write your code here
        t -= 30
        ret = []
        ans = 0
        print t
        
        dur.sort()
        
        for i in range(len(dur)-1, -1, -1):
            if dur[i] < t:
                tmp = self.find(dur, t-dur[i], i-1)
                print tmp, dur[i], t-dur[i], ans
                if tmp <= t-dur[i] and tmp + dur[i] > ans:
                    ans = tmp + dur[i]
                    if len(ret) > 0:
                        ret.pop()
                        ret.pop()
                    ret.append(tmp)
                    ret.append(dur[i])
                        
        return ret
                    
                
    def find(self, dur, need, pos):
        l = 0
        r = pos
        if r == -1:
            return dur[0]
        
        while l < r:
            mid = (l+r)/2
            if dur[mid] == need:
                return need
            elif dur[mid] < need:
                l = mid+1
            else:
                r = mid
                
        if dur[l] > need:
            return dur[l-1]
        else:
            return dur[l]

if __name__ == '__main__':
    s = 127
    v = [50,17,46,42,22,28,13,12,54,52,19,12]
    s = 60
    v = [15,15,16,13]
    ss = Solution()
    print "answer is\n"
    print ss.aerial_Movie(s, v)
