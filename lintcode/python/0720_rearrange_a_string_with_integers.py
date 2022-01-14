#!/usr/bin/python3 -t

# string

class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, str):
        # Write your code here
        n = len(str)
        ret = ""
        d = {}
        cnt = 0
        for s in str:
            if  "0" <= s <= "9":
                cnt += int(s)
                continue
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1

        for i in range(26):
            key = chr(i + ord("A"))
            if key in d:
                val = d[key]
                while val > 0:
                    ret += key
                    val -= 1

        if cnt != 0:
            #print(cnt)
            ret = ret + "{}".format(cnt)

        return ret

        
if __name__ == '__main__':
    s = Solution()
    a = "AC2BEW3"
    print(s.rearrange(a))